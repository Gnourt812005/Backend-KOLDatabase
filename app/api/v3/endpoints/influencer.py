from fastapi import APIRouter, Depends, HTTPException, status 
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from app.core.database import get_database

from app.crud.influencer import influencer_crud
from app.models.influencer import Influencer
from app.models.field import Field
from app.models.platform import Platform
from app.models.influencer_field import InfluencerField
from app.models.influencer_platform import InfluencerPlatform
from app.schemas.influencer import InfluencerOut
from typing import List 
from uuid import UUID 
from sqlalchemy import text, select, func, distinct

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/influencer", response_model=List[InfluencerOut], response_model_exclude_unset=True)
async def get_all(db: Session = Depends(get_database)):
    try:
        data = (db.query(
                        Influencer,
                        func.array_agg(distinct(Field.name)).label("field"),
                        func.array_agg(distinct(Platform.name)).label("platform")
                    ).select_from(Influencer)
                    .join(InfluencerField, Influencer.id == InfluencerField.influencer_id)
                    .join(Field, InfluencerField.field_id == Field.id)
                    .join(InfluencerPlatform, Influencer.id == InfluencerPlatform.influencer_id)
                    .join(Platform, InfluencerPlatform.platform_id == Platform.id)
                    .group_by(*[getattr(Influencer, col.name) for col in Influencer.__table__.columns]))
        print(data[0])
        response = []

        for influencer, field, platform in data:
            serialized = jsonable_encoder(influencer, exclude_unset=True, exclude={"description_vector"})
            serialized["field"] = field
            serialized["platform"] = platform
            response.append(serialized)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Server error")

    return response

@router.get("/influencer/{id}", response_model=InfluencerOut, response_model_exclude_unset=True)
async def get(id : UUID, db: Session = Depends(get_database)):
    try:
        data = influencer_crud.get(db=db, id=id)
        if data is None:
            raise HTTPException(status_code=404, detail="Influencer not found")
        data_platform = (db.query(func.array_agg(distinct(Platform.name))).select_from(InfluencerPlatform)
                         .join(Platform, InfluencerPlatform.platform_id == Platform.id)
                         .filter(InfluencerPlatform.influencer_id == data.id)
                         .group_by(InfluencerPlatform.influencer_id).all())
        data_field = (db.query(func.array_agg(distinct(Field.name))).select_from(InfluencerField)
                         .join(Field, InfluencerField.field_id == Field.id)
                         .filter(InfluencerField.influencer_id == data.id)
                         .group_by(InfluencerField.influencer_id).all())
        response = jsonable_encoder(data, exclude={"description_vector"})

        response["field"] = data_field[0][0]
        response["platform"] = data_platform[0][0]
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Server error") 