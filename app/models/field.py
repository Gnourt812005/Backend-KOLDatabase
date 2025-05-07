from sqlalchemy import Column, String, PrimaryKeyConstraint, UniqueConstraint, Unicode
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base 
from app.models.influencer_field import InfluencerField

class Field(Base):
    __tablename__ = "field"

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"))
    name = Column(Unicode, nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_field"),
        UniqueConstraint("name", name="uq_field_name"),
    )

    rlts_influencer_field = relationship("InfluencerField", foreign_keys=[InfluencerField.field_id], back_populates="rlts_field")
