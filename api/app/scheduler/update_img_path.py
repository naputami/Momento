from app.models.post import Posts
from app.extentions import client, db
from app.post.helper import BUCKET_NAME
from datetime import timedelta

def update_img_path():
    posts = Posts.query.all()

    for post in posts:
        post.img_path = client.presigned_get_object(BUCKET_NAME, post.img_name, expires=timedelta(days=7))
    
    db.session.commit()
