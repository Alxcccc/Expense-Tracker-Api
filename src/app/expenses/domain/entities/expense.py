from pydantic import BaseModel
from typing import Optional

from src.app.expenses.domain.value_objects.expense_title import ExpenseTitle
from src.app.expenses.domain.value_objects.expense_date import ExpenseDate
from src.app.expenses.domain.value_objects.expense_description import ExpenseDescription
from src.app.expenses.domain.value_objects.expense_category import ExpenseCategory
from src.app.expenses.domain.value_objects.expense_amount import ExpenseAmount
from src.app.expenses.domain.value_objects.expense_id_user import ExpenseIdUser

class Expense(BaseModel):
    id_expense: Optional[int]
    expense_title: ExpenseTitle
    expense_date: ExpenseDate
    description: ExpenseDescription
    category: ExpenseCategory
    amount: ExpenseAmount
    idUser: ExpenseIdUser
    