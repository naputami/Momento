from app.extentions import db
from app.models.base import Base
from sqlalchemy.dialects.postgresql import UUID

class Posts(Base):

    __tablename__ = "posts"

    content = db.Column(db.Text, nullable=False)
    img_name = db.Column(db.String(255), nullable=True)
    img_path = db.Column(db.String(255), nullable=True)
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

