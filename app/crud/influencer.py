from app.schemas.influencer import InfluencerCreate, InfluencerUpdate
from app.models.influencer import Influencer

from app.crud.base import BaseCRUD

class InfluencerCRUD(BaseCRUD[Influencer, InfluencerCreate, InfluencerUpdate]):
    pass 

influencer_crud = InfluencerCRUD(Influencer)

