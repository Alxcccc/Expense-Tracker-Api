from pydantic import BaseModel, EmailStr
from typing import Optional

from src.app.users.domain.value_objects.user_id import UserId
from src.app.users.domain.value_objects.user_username import UserUsername
from src.app.users.domain.value_objects.user_password import UserPassword
from src.app.users.domain.value_objects.user_email import UserGmail

class User(BaseModel):
    id_user: Optional[UserId]
    username: UserUsername
    password: UserPassword
    gmail: UserGmail
    
class UserCreate(BaseModel):
    username: UserUsername
    password: UserPassword
    gmail: UserGmail
    
