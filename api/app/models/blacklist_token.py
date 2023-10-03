from app.extentions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BlacklistTokens(db.Model):

    __tablename__ = "blacklist_tokens"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    jti = db.Column(db.String(36), nullable = False, unique = True)

    def serialize(self):
        return {
            "id": self.id,
            "jti": self.jti
        }