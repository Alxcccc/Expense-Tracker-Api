from typing import Optional
from sqlmodel import Field, SQLModel

class UserDatabase(SQLModel, table=True):
    __tablename__ = "users"
    id_user: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    gmail: str