from app.extentions import db
from app.models.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import event
from datetime import datetime, timedelta

class Posts(Base):

    __tablename__ = "posts"

    content = db.Column(db.Text, nullable=False)
    img_name = db.Column(db.String(500), nullable=True)
    img_path = db.Column(db.String(500), nullable=True)
    img_expiration_date = db.Column(db.DateTime)
    likes = db.Column(db.Integer, default=0)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    user = db.relationship("Users", back_populates="posts")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "img_name": self.img_name,
            "img_path": self.img_path,
            "likes": self.likes,
            "username": self.user.username
        }

@event.listens_for(Posts, 'before_insert')
def set_default_expiration_date(mapper, connection, target):
    if target.img_path:  
        target.img_expiration_date = datetime.utcnow() + timedelta(days=7)