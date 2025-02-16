from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date

class UserDatabase(SQLModel, table=True):
    __tablename__ = "users"
    id_user: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: date
    gmail: str