from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date

class ExpenseDatabase(SQLModel, table=True):
    __tablename__ = "expenses"
    id_expense: Optional[int] = Field(default=None, primary_key=True)
    expense_title: str
    expense_date: date
    description: str
    category: str
    amount: int
    idUser: Optional[int] = Field(default=None, foreign_key="users.id_user")