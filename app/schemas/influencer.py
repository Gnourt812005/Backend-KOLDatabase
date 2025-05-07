from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, List 
from datetime import date
from uuid import UUID 

class InfluencerBase(BaseModel):
    name: str
    location: Optional[str] = None 
    description: Optional[str] = None 
    description_vector: Optional[List[float]] = None  

class InfluencerCreate(InfluencerBase):
    pass 

class InfluencerUpdate(BaseModel):
    name: Optional[str] = None 
    location: Optional[str] = None 
    description: Optional[str] = None 
    description_vector: Optional[List[float]] = None 

class InfluencerOut(BaseModel):
    id: Optional[UUID] = None 
    name: Optional[str] = None 
    location: Optional[str] = None 
    description: Optional[str] = None
    field : Optional[List[str]] = None 
    platform : Optional[List[str]] = None
    created_at : Optional[date] = None 
    updated_at : Optional[date] = None  

    model_config = ConfigDict(from_attributes=True) 

