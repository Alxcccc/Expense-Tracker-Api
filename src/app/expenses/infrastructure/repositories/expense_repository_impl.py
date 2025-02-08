from typing import List, Optional, Union
from sqlmodel import Session, select

# Entity
from src.app.expenses.domain.entities.expense import Expense

# Repository
from src.app.expenses.domain.repositories.expense_repository import ExpenseRepository

# Database
from src.app.infrastructure.database.database import DataBase

# DB model
from src.app.infrastructure.database.models.expense_model import ExpenseDatabase

# value objects
from src.app.expenses.domain.value_objects.expense_title import ExpenseTitle
from src.app.expenses.domain.value_objects.expense_date import ExpenseDate
from src.app.expenses.domain.value_objects.expense_description import ExpenseDescription
from src.app.expenses.domain.value_objects.expense_category import ExpenseCategory
from src.app.expenses.domain.value_objects.expense_amount import ExpenseAmount

class ExpenseRepositoryImpl(ExpenseRepository):
    def get_all(self) -> List[ExpenseDatabase]:
        try:
            with Session(DataBase.engine) as session:
                statement = select(ExpenseDatabase)
                results = session.exec(statement).all()
                result = list()
                for expense in results:
                    result.append(
                        {
                        "id_expense": expense.id_expense,
                        "expense_title": expense.expense_title,
                        "expense_date": expense.expense_date,
                        "description": expense.description,
                        "category": expense.category,
                        "amount": expense.amount,
                        "idUser": expense.idUser
                    }
                        )
                return result
            
        except Exception as e:
            print(e)
    
    def get_by_id(self, id_expense: int) -> Expense:
        pass
    
    def create(self, expense: Expense) -> Expense:
        pass
    
    def update(self, id_expense: int, expense: Expense) -> Expense:
        pass
    
    def delete(self, id_expense: int) -> bool:
        pass