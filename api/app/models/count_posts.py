from app.extentions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CountPosts(db.Model):

    __tablename__ = "count_posts"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String(80), unique=True, nullable=False)
    count_posts = db.Column(db.Integer, default=0)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "countPosts": self.count_posts 
        }