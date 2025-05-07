from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.logger import setup_logger
from app.core.config import settings
from app.core.database import engine, Base

# from app.api.v1 import router_v1
from app.api.v2 import router_v2
import time 
import logging
setup_logger()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Run successfully")
        with engine.connect() as db:
            logger.info("Successfiully connect to database")
            # Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.error(f"Error: {e}")
    yield
    # Base.metadata.drop_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan = lifespan
)

origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allows requests from the specified origins
    allow_credentials=True,          # Allows cookies and credentials
    allow_methods=["*"],             # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allows all headers
)

# app.include_router(router_v1, prefix="/api/v1")
app.include_router(router_v2, prefix="/api/v2")

@app.middleware("http")
async def log_request(request : Request, call_next):
    start = time.time()
    response = await call_next(request)

    logger.info(f"{request.method} completed in {(time.time() - start):2f}s")
    return response


@app.get("/test")
async def test():
    return {"Test" : "Server is running"}