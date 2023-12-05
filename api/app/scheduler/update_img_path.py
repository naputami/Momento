from sqlalchemy import and_
from app.models.post import Posts
from app.extentions import client, db
from app.post.helper import BUCKET_NAME
from datetime import timedelta, datetime
import pytz

def update_img_path():
    current_time =  datetime.now(pytz.timezone('Asia/Jakarta'))
    posts_with_image = Posts.query.filter(Posts.img_path.isnot(None)).all()


    for post in posts_with_image:
        if post.img_expiration_date <= current_time:
            try:
                post.img_path = client.presigned_get_object(BUCKET_NAME, post.img_name, expires=timedelta(days=7))
                post.img_expiration_date = current_time + timedelta(days=7)
                db.session.add(post)
            except:
                print("There's error in updating image url")

    db.session.commit()
