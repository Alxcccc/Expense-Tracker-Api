from pydantic import BaseModel
from typing import Optional

from src.app.users.domain.value_objects.user_id import UserId

class User(BaseModel):
    id_user = Optional[UserId]
    username = str
    password = str
    gmail = str
    
class UserCreate(BaseModel):
    username = str
    password = str
    gmail = str
    
