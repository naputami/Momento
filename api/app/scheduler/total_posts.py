from app.models.user import Users
from app.models.post import Posts
from app.models.count_posts import CountPosts
from app.extentions import db

def count_posts():
    users = Users.query.all()
    user_posts = {}
    for user in users:
        post_count = Posts.query.filter_by(user_id=user.id).count()
        user_posts[user.username] = post_count
    
    # sorted_users = sorted(user_posts.items(), key=lambda x:x[1], reverse=True)

    existing_trending_users = CountPosts.query.all()
    existing_users = {trending_user.username: trending_user for trending_user in existing_trending_users}

    for username, post_count in user_posts.items():
        if username in existing_users:
            trending_user = existing_users[username]
            trending_user.count_posts = post_count
        else:
            trending_user = CountPosts(username=username, count_posts=post_count)
            db.session.add(trending_user)
        
    db.session.commit()