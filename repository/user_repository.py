from sqlalchemy import Integer, select
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import set_attribute

from core.crypto import hash_email, encrypt_field
from core.security import get_password_hash
from model.user import User
from repository.user_repository_interface import IUserRepository
from repository.base import ModelType, UpdateSchemaType, CreateSchemaType
from schema.user import UserSchemaCreate, UserSchemaUpdate


class UserRepository(IUserRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> User | None:
        """
        Get user by email
        :param email:
        :return:
        """
        try:
            hashed_email = hash_email(email)
            stmt = select(User).where(User.hashed_email == hashed_email)
            return self.session.scalars(stmt).first()
        except Exception as e:
            print(f"Error occurred while fetching user by email: {e}")
            return None

    def exists_by_email(self, email: str) -> bool:
        """
        Checks whether the user with an email exists or not.
        :param email:
        :return:
        """
        try:
            hashed_email = hash_email(email)
            stmt = select(User).where(User.hashed_email == hashed_email)
            return self.session.scalars(stmt).first() is not None
        except Exception as e:
            print(f"Error occurred while fetching user by email: {e}")
            return False


    def get_by_id(self, id: Integer) -> User | None:
        """
        Get a user by id
        :param id:
        :return:
        """
        try:
            stmt = select(User).where(User.id == id)
            return self.session.scalars(stmt).first()
        except Exception as e:
            print(f"Error occurred while fetching user by id: {e}")
            return None

    def create(self, obj_in: UserSchemaCreate) -> User:
        """
        Creates a new user in the database
        :param obj_in:
        :return:
        """
        raw_email = obj_in.email.strip().lower()
        try:
            db_user = User(
                username=obj_in.username,
                hashed_email=hash_email(raw_email),
                email=encrypt_field(raw_email),
                password=get_password_hash(obj_in.password),
                fullname=obj_in.fullname,
                is_active=obj_in.is_active
            )
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)
            return db_user
        except Exception as e:
            print(f"Error occurred while creating user: {e}")
            return None

    def update(self, db_obj: User, obj_in: UserSchemaUpdate) -> User:
        """
        Performs an update information to the database user
        :param db_obj:
        :param obj_in:
        :return:
        """
        update_data = obj_in.model_dump(exclude_unset=True)
        try:
            if "password" in update_data and update_data["password"]:
                update_data["password"] = get_password_hash(update_data["password"])

            if "email" in update_data and update_data["email"]:
                raw_email = update_data["email"].strip().lower()
                update_data["email"] = encrypt_field(raw_email)
                update_data["hashed_email"] = hash_email(raw_email)

            for field,value in update_data:
                # set data in the database object that is to be commited
                setattr(db_obj,field,value)

            self.session.commit()
            self.session.refresh(db_obj)
            return db_obj
        except Exception as e:
            print(f"Error occurred while updating user: {e}")
            return None


    def delete(self, id: Integer) -> bool:
        """
        Deletes the user from the database.
        :param id:
        :return:
        """
        try:
            stmt = select(User).where(User.id == id)
            db_user = self.session.scalars(stmt).first()
            self.session.delete(db_user)
            self.session.commit()
            return db_user
        except Exception as e:
            print(f"Error occurred while deleting user: {e}")
            return None