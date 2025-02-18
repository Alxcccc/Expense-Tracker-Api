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
from src.app.users.domain.value_objects.user_email import UserGmail

class UserRepositoryImpl(UserRepository):
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def crypt_password(cls, password: str):
        password = cls.context.hash(password)
        return password
    
    def crypt_verify(cls, username, password):
        try:
            with Session(DataBase.engine) as session:
                statement = select(UserDatabase).where(UserDatabase.username == username)
                user = session.exec(statement).one()
                return cls.context.verify(password, user.password)
            
        except NoResultFound:
            return None
        
        except Exception as e:
            raise Exception(str(e))
        
    def login(self, username, password) -> Optional[User]:
        try:
            with Session(DataBase.engine) as session:
                verify = self.crypt_verify(username, password)
                if verify:
                    statement = select(UserDatabase).where(UserDatabase.username == username)
                    user = session.exec(statement).one()
                    return user.id_user
                raise ValueError("The credentials are wrong")
        except Exception as e:
            raise Exception(str(e))
        
    def get_by_id(self, id_user: int) -> Optional[User]:
        try:
            with Session(DataBase.engine) as session:
                statement = select(UserDatabase).where(UserDatabase.id_user == id_user)
                user = session.exec(statement).one()
                return User(id_user=UserId(value=user.id_user), username=UserUsername(value=user.username), password=UserPassword(value=user.password), gmail=UserGmail(value=user.gmail))
            
        except NoResultFound:
            return None
        
        except Exception as e:
            raise Exception(str(e))
    
    def create(self, user: UserCreate) -> Union[User, bool]:
        try:
            with Session(DataBase.engine) as session:
                crypt_password = self.crypt_password(user.password.value)
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