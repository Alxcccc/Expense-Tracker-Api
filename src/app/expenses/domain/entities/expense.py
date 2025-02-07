from pydantic import BaseModel
from typing import Optional

from src.app.expenses.domain.value_objects.expense_date import ExpenseDate
from src.app.expenses.domain.value_objects.expense_description import ExpenseDescription
from src.app.expenses.domain.value_objects.expense_category import ExpenseCategory
from src.app.expenses.domain.value_objects.expense_amount import ExpenseAmount

class Expense(BaseModel):
    id: Optional[int]
    expense_date: ExpenseDate
    description: ExpenseDescription
    category: ExpenseCategory
    amount: ExpenseAmount