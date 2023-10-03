from app.extentions import db
from app.count_posts import countPostBp
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.count_posts import CountPosts
from sqlalchemy import desc

@countPostBp.route("", methods=['GET'], strict_slashes = False)
@jwt_required(locations=["headers"],optional=True)
def get_count_posts():
    limit = request.args.get('limit', 20)
    if type(limit) is not int:
        return jsonify({'message': 'invalid parameter'}), 400
    
    user_id = get_jwt_identity()

    if not user_id:
        return jsonify({
            "message": "You should login first!"
        }), 401

    count_posts = db.session.execute(
        db.select(CountPosts).limit(limit).order_by(desc(CountPosts.count_posts))
    ).scalars()

    results = []
    for count_post in count_posts:
        results.append(count_post.serialize())

    response = make_response(jsonify(
        data=results
    ), 200)

    return response