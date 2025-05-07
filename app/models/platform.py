from sqlalchemy import Column, String, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base 
from app.models.influencer_platform import InfluencerPlatform

class Platform(Base):
    __tablename__ = "platform"

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_platform"),
        UniqueConstraint("name", name="uq_platform_name"),
    )

    rlts_influencer_platform = relationship("InfluencerPlatform", foreign_keys=[InfluencerPlatform.platform_id], back_populates="rlts_platform")
