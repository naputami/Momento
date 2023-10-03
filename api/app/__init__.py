from flask import Flask
from config import Config
from app.extentions import db, migrate, jwt, login_manager
from app.auth import authBp
from app.post import postBp
from app.count_posts import countPostBp
from app.frontend import frontendBp
from app.models.user import Users
from app.models.post import Posts
from flask_admin import Admin
from app.admin.MyModelView import CustomModelView, AdminModelView

import schedule
import time
import threading


def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)
    
    admin = Admin(app, name='Dashboard', template_mode='bootstrap4', index_view=AdminModelView('home'), url="/")
    admin.add_view(CustomModelView(Users, db.session))
    admin.add_view(CustomModelView(Posts, db.session))

    def schedule_count_tweets():
        with app.app_context():
            from app.scheduler.total_posts import count_posts
            count_posts()
            print("Periodic Task Running")
    
    schedule.every(60).seconds.do(schedule_count_tweets)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    app.register_blueprint(authBp, url_prefix="/api/auth")
    app.register_blueprint(postBp, url_prefix="/api/posts")
    app.register_blueprint(countPostBp, url_prefix='/api/count_posts')
    app.register_blueprint(frontendBp, url_prefix="/")

    return app
