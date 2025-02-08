from typing import Optional
from sqlmodel import Field, SQLModel

from src.app.expenses.domain.value_objects.expense_title import ExpenseTitle
from src.app.expenses.domain.value_objects.expense_date import ExpenseDate
from src.app.expenses.domain.value_objects.expense_description import ExpenseDescription
from src.app.expenses.domain.value_objects.expense_category import ExpenseCategory
from src.app.expenses.domain.value_objects.expense_amount import ExpenseAmount

class ExpenseDatabase(SQLModel, table=True):
    id_expense: Optional[int] = Field(default=None, primary_key=True)
    expense_title: ExpenseTitle
    expense_date: ExpenseDate
    description: ExpenseDescription
    category: ExpenseCategory
    amount: ExpenseAmount