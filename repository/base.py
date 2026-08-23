from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import Integer
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

class AbstractRepository(ABC, Generic[ModelType,CreateSchemaType,UpdateSchemaType]):

    def __init__(self, session:Session):
        self.session = session

    @abstractmethod
    def get_by_id(self,id: Integer) -> ModelType | None:
        pass

    @abstractmethod
    def create(self, obj_in:CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def update(self, db_obj:ModelType, obj_in:UpdateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def delete(self, id: Integer) -> bool:
        pass