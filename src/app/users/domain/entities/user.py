from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id_user = Optional[int]
    username = str
    password = str
    gmail = str
    
class UserCreate(BaseModel):
    username = str
    password = str
    gmail = str
    
