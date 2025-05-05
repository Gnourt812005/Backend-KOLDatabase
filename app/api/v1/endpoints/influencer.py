from fastapi import APIRouter, Depends, HTTPException, status 
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from app.core.database import get_database

from app.crud.influencer import influencer_crud
from app.models.influencer import Influencer
from app.schemas.influencer import InfluencerOut
from typing import List 
from sqlalchemy import text, select
from app.services.embedding import embedding_client

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_model=List[InfluencerOut])
async def get_all(db: Session = Depends(get_database)):
    try:
        response = influencer_crud.get_all(db=db)
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    

@router.get("/update_vector", response_model=List[InfluencerOut])
async def get_all(db: Session = Depends(get_database)):
    try:
        response = influencer_crud.get_all(db=db)
        for row in response:
            if not row.description:
                logger.warning(f"Row with ID {row.id} is missing 'description'. Skipping.")
                continue

            if row.description_vector is None:
                row.description_vector = embedding_client.encode(row.description)

        db.commit() 
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/find", response_model=List[InfluencerOut])
async def search_similar_influencers(query_str: str, db: Session = Depends(get_database)):
    vector_str = embedding_client.encode(query_str)

    result = select(Influencer).order_by(Influencer.description_vector.cosine_distance(vector_str)).limit(5)
    return db.execute(result).scalars().all()