from abc import abstractmethod

from model.user import User
from repository.base import AbstractRepository
from schema.user import UserSchemaCreate, UserSchemaUpdate


class IUserRepository(AbstractRepository[User, UserSchemaCreate, UserSchemaUpdate]):

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass