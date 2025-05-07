from sqlalchemy import Column, Integer, String, Date, PrimaryKeyConstraint, Unicode, Text
from pgvector.sqlalchemy import Vector
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base 

from app.models.influencer_field import InfluencerField
from app.models.influencer_platform import InfluencerPlatform

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

    rlts_influencer_field = relationship("InfluencerField", foreign_keys=[InfluencerField.influencer_id], back_populates="rlts_influencer")
    rlts_influencer_platform = relationship("InfluencerPlatform", foreign_keys=[InfluencerPlatform.influencer_id], back_populates="rlts_influencer")

