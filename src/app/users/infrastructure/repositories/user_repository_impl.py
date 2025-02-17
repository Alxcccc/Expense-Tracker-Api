from typing import Optional, Union
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound

# Crypt
from passlib.context import CryptContext

# Entity
from src.app.users.domain.entities.user import User, UserCreate

# Repository
from src.app.users.domain.repositories.user_repository import UserRepository

# Database
from src.app.infrastructure.database.database import DataBase

# DB model
from src.app.infrastructure.database.models.user_model import UserDatabase

# value objects
from src.app.users.domain.value_objects.user_id import UserId
from src.app.users.domain.value_objects.user_username import UserUsername
from src.app.users.domain.value_objects.user_password import UserPassword

class UserRepositoryImpl(UserRepository):
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def crypt_password(cls, password: str):
        password = cls.context.hash(password)
        print(type(password))
        return password
    
    def crypt_verify(cls, username, password):
        try:
            with Session(DataBase.engine) as session:
                statement = select(UserDatabase).where(UserDatabase.username == username)
                user = session.exec(statement).one()
                if not user:
                    return None
                return cls.context.verify(password, user.password)
        except Exception as e:
            raise Exception(str(e))

    def get_by_id(self, id_user: int) -> Optional[User]:
        try:
            with Session(DataBase.engine) as session:
                statement = select(UserDatabase).where(UserDatabase.id_user == id_user)
                user = session.exec(statement).one()
                if not user:
                    return None
                return User(id_user=UserId(value=user.id_user), username=UserUsername(value=user.username), password=UserPassword(value=user.password), gmail=user.gmail)
        except Exception as e:
            raise Exception(str(e))
    
    def create(self, user: UserCreate) -> Union[User, bool]:
        try:
            with Session(DataBase.engine) as session:
                crypt_password = crypt_password(user.password.value)
                new_user = UserDatabase(username=user.username, password=crypt_password, gmail=user.gmail)
                session.add(new_user)
                session.commit()
        except Exception as e:
            raise Exception(str(e))
    
    def delete(self, id_user: int) -> bool:
        try:
            with Session(DataBase.engine) as session:
                statement = select(UserDatabase).where(UserDatabase.id_user == id_user)
                user = session.exec(statement).one()
                session.delete(user)
                session.commit()
            
        except Exception as e:
            raise Exception(str(e))