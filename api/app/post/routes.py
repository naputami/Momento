from flask import jsonify, request
from app.extentions import db, client
from app.models.post import Posts
from app.models.user import Users
from app.post import postBp
from flask_jwt_extended import jwt_required, get_jwt_identity
from minio import Minio
from datetime import timedelta
from werkzeug.utils import secure_filename
import os
from app.post.helper import allowed_file, BUCKET_NAME


# endpoint for getting all posts
# user can see all posts without login
@postBp.route("", methods=['GET'], strict_slashes=False)
def get_all_post():

    limit = request.args.get('limit', 100)

    if type(limit) is not int:
        return jsonify({'message': 'invalid parameter'}), 400
    
    posts = db.session.execute(db.select(Posts).limit(limit)).scalars()

    data = [post.serialize() for post in posts]

    response = jsonify({
        "posts": data
    })

    return response, 200


# endpoint for getting all posts from one user
@postBp.route("/<user_id>", methods=['GET'], strict_slashes=False)
def get_one_user_posts(user_id):

    limit = request.args.get('limit', 20)

    if type(limit) is not int:
        return jsonify({'message': 'invalid parameter'}), 400
    
    posts = db.session.query(Posts).filter(Posts.user_id==user_id).limit(limit)

    data = [post.serialize() for post in posts]

    response = jsonify({
        "posts": data
    })

    return response, 200

# endpoint for creating a new post
# user must log in to create a new post
@postBp.route("", methods=['POST'], strict_slashes=False)
@jwt_required(locations=["headers"])
def create_post():

    user_id = get_jwt_identity()

    if not user_id:
        return jsonify({
            "message": "You must login to create a post!"
        }), 401
    
    found = client.bucket_exists(BUCKET_NAME)

    if not found:
        client.make_bucket(BUCKET_NAME)
    else:
        print("Bucket already exists")
    
    if 'file' in request.files:
        file = request.files['file']
        expiration_time = timedelta(days=7)
        if file and allowed_file(file.filename):
            content = request.form.get('content')
            user_id = get_jwt_identity()
            image_name = secure_filename(file.filename)
            image_size = os.fstat(file.fileno()).st_size
            client.put_object(BUCKET_NAME, image_name, file, image_size)
            image_path = client.presigned_get_object(BUCKET_NAME, image_name, expires=expiration_time)
            new_content = Posts(content=content, img_name=image_name, img_path=image_path, user_id=user_id)
            db.session.add(new_content)
            db.session.commit()
            response = jsonify(success = True, message ='New post is created!', post = new_content.serialize())
            return response, 200


    data = request.get_json()

    content = data.get("content")
    img_name = data.get("img_name", None)
    img_path = data.get("img_path", None)


    if not content:
        return jsonify({'error': 'Missing content'}), 400


    new_post = Posts(
        content=content,
        img_name=img_name,
        img_path=img_path,
        user_id=user_id
    )

    db.session.add(new_post)
    db.session.commit()

    response = jsonify({
    "success": True,
    "message": 'New post is created!',
    "post": new_post.serialize()
    })

    return response, 200

# endpoint for editing a post
@postBp.route("/<post_id>", methods=['PATCH'], strict_slashes=False)
@jwt_required(locations=["headers"])
def edit_post(post_id):
    data = request.get_json()

    new_content = data.get("content")
    new_img_name = data.get("img_name", None)
    new_img_path = data.get("img_path", None)


    if not new_content:
        return jsonify({'error': 'Missing content'}), 400

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({
            "message": "You must login to edit a post!"
        }), 401

    post = db.session.query(Posts).filter_by(id=post_id).first()

    if not post:
        return jsonify({
            "success": False,
            "message": "Post not found!"
        }), 404
    
    # casting to string for comparing value only
    if current_user != str(post.user_id):
        return jsonify({
            "message":f'You do not have permission to edit this post.'
        }), 403
    
    post.content = new_content
    post.img_name = new_img_name
    post.img_path = new_img_path
    db.session.commit()

    response = jsonify({
            "success": True,
            "message" : f'post with id {post_id} has been changed',
            "post" : post.serialize()
    })

    return response, 200

# endpoint for deleting a post
@postBp.route("/<post_id>", methods=['DELETE'], strict_slashes=False)
@jwt_required(locations=["headers"])
def delete_post(post_id):
    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({
            "message": "You must login to delete a post!"
        }), 401

    post = db.session.query(Posts).filter_by(id=post_id).first()

    if not post:
        return jsonify({
            "success": False,
            "message": "Post not found!"
        }), 404
    
    # casting to string for comparing value only
    if current_user != str(post.user_id):
        return jsonify({
            "message":f'You do not have permission to delete this post.'
        }), 403
    
    db.session.delete(post)
    db.session.commit()

    response = jsonify({
            "success": True,
            "message" : f'post with id {post_id} has been deleted'
    })

    return response, 200
    


# endpoint for liking a post
@postBp.route("/<post_id>/like", methods=['POST'], strict_slashes=False)
@jwt_required(locations=["headers"])
def like_post(post_id):

    user_id = get_jwt_identity()

    if not user_id:
        return jsonify({
            "message": "You must login to like a post!"
        }), 401

    post = db.session.query(Posts).filter_by(id=post_id).first()

    if post:
        post.likes += 1
        db.session.commit()
        return jsonify({
            'message': 'Post is liked successfully',
            'post': post.serialize()
            }), 200
    else:
        return jsonify({'error': 'Post not found'}), 404

# endpoint for disliking a post
@postBp.route("/<post_id>/dislike", methods=['POST'], strict_slashes=False)
@jwt_required(locations=["headers"])
def dislike_post(post_id):

    user_id = get_jwt_identity()

    if not user_id:
        return jsonify({
            "message": "You must login to dislike a post!"
        }), 401


    post = db.session.query(Posts).filter_by(id=post_id).first()

    if post:
        post.likes -= 1
        db.session.commit()
        return jsonify({
            'message': 'Post is disliked successfully',
            'post': post.serialize()
            }), 200
    else:
        return jsonify({'error': 'Post not found'}), 404