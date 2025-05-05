from sqlalchemy import Column, String, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base 

class Platform(Base):
    __tablename__ = "platform"

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_platform"),
        UniqueConstraint("name", name="uq_platform_name"),
    )