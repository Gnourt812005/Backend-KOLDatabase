from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional, Union
from uuid import UUID
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseCRUD (Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__ (self, model : Type[ModelType]):
        self.model = model 

    def get (self, db: Session, id: Union[int, UUID]) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all (self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create (self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj = self.model(**obj_in.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def update (self, db : Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj 
    
    def delete (self, db: Session, id: Union[int, UUID]) -> Optional[ModelType]:
        obj = self.get(db, id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj 