from fastapi.params import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from repository.user_repository import UserRepository
from repository.user_repository_interface import IUserRepository


def get_user_repository(
        db:Session = Depends(get_db)
) -> IUserRepository:
    return UserRepository(db)