from app.models.post import Posts
from app.extentions import db
from app.models.base import Base

class Users(Base):

    __tablename__ = "users"

    name = db.Column(db.String(124), nullable=False)
    username = db.Column(db.String(124), nullable=False, unique=True)
    email = db.Column(db.String(123), nullable=False, unique=True)
    password_hash = db.Column(db.String(1024), nullable=False, unique=True)
    role = db.Column(db.String(10), nullable=False)
    posts = db.relationship('Posts', back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email
        }


