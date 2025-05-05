from sqlalchemy import Column, String, Integer, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint, CheckConstraint
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base 

class InfluencerPlatform(Base):
    __tablename__ = "influencer_platform"

    influencer_id = Column(UUID(as_uuid=True))
    platform_id = Column(UUID(as_uuid=True))
    is_primary = Column(Boolean, server_default=text("false"))
    url = Column(String)
    followers_count = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("influencer_id", "platform_id", name="pk_influencer_platform"),
        ForeignKeyConstraint(["influencer_id"], ["influencer.id"], name="fk_influencer_platform_influencer_id"),
        ForeignKeyConstraint(["platform_id"], ["platform.id"], name="fk_influencer_platform_platform_id"),
        
        CheckConstraint("followers_count >= 0", name="ck_influencer_platform_followers_count"),
    )
