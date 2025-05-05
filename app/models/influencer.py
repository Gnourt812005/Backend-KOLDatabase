from sqlalchemy import Column, Integer, String, Date, PrimaryKeyConstraint, Unicode, Text
from pgvector.sqlalchemy import Vector
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base 

class Influencer(Base):
    __tablename__ = "influencer"

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"))
    name = Column(Unicode, nullable=False)
    location = Column(Unicode)
    description = Column(Unicode(1000))
    description_vector = Column(Vector(384))

    created_at = Column(Date, server_default=func.now()) 
    updated_at = Column(Date, server_default=func.now()) 

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_influencer"),
    )
