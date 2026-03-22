from sqlalchemy import Column, String, DateTime, Integer, CheckConstraint, ForeignKey, Index
from sqlalchemy.sql import func
from src.database.base import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("LENGTH(title) > 0"),
        CheckConstraint("LENGTH(content) > 0"),
        Index("idx_notes_user_id", "user_id"),
    )
