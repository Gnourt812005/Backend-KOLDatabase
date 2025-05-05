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
    name: str
    location: Optional[str] = None 
    description: Optional[str] = None 
    id: UUID
    created_at : date
    updated_at : date 

    model_config = ConfigDict(from_attributes=True) 

