from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.logger import setup_logger

from app.core.database import engine, Base
from app.models.influencer_platform import InfluencerPlatform

from app.api.v1 import router_v1

import logging
setup_logger()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Run successfully")
        with engine.connect() as db:
            logger.info("Successfiully connect to database")
            Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.error(f"Error: {e}")
    yield
    Base.metadata.drop_all(bind=engine)

app = FastAPI(
        lifespan = lifespan 
    )

app.include_router(router_v1, prefix="/api/v1")

@app.get("/test")
async def test():
    return {"Test" : "Server is running"}