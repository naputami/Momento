from app.extentions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
import uuid

class Base(db.Model):

    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())