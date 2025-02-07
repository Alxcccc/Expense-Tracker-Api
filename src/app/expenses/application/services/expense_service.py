from typing import List, Optional, Union

# Repositories
from src.app.expenses.domain.repositories.expense_repository import ExpenseRepository

# Entities
from src.app.expenses.domain.entities.expense import Expense

class ExpenseService:
    
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository
        
    def get_all(self) -> List[Expense]:
        return self.expense_repository.get_all()
    
    def get_by_id(self, id_expense: int) -> Expense:
        return self.expense_repository.get_by_id(id_expense)
    
    def create(self, expense: Expense) -> Expense:
        return self.expense_repository.create(expense)
    
    def update(self, id_expense: int, expense: Expense) -> Expense:
        return self.expense_repository.update(id_expense, expense)
    
    def delete(self, id_expense: int) -> bool:
        return self.expense_repository.delete(id_expense)