from sqlalchemy import Column, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base 

class InfluencerField(Base):
    __tablename__ = "influencer_field"

    influencer_id = Column(UUID(as_uuid=True))
    field_id = Column(UUID(as_uuid=True))
    is_primary = Column(Boolean, server_default=text("false"))
    __table_args__ = (
        PrimaryKeyConstraint("influencer_id", "field_id", name="pk_influencer_field"),
        ForeignKeyConstraint(["influencer_id"], ["influencer.id"], name="fk_influencer_field_influencer_id"),
        ForeignKeyConstraint(["field_id"], ["field.id"], name="fk_influencer_field_field_id"),
        
    )

    rlts_influencer = relationship("Influencer", foreign_keys=influencer_id, back_populates="rlts_influencer_field")
    rlts_field = relationship("Field", foreign_keys=field_id, back_populates="rlts_influencer_field")

