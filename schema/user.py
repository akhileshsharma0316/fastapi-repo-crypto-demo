from datetime import datetime

from pydantic import BaseModel


class UserSchemaBase(BaseModel):
    username: str
    email: str
    password: str
    fullname: str | None = None
    is_active: bool = True

class UserSchemaCreate(UserSchemaBase):
    pass

class UserSchemaUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    fullname: str | None = None
    is_active: bool | None = None


class UserSchemaRead(BaseModel):
    # TODO: Ensure when returning information pop up the fields from the Base Schema Dictionary
    id: int
    username: str
    fullname: str | None = None
    created_at: datetime
    updated_at: datetime