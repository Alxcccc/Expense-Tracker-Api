from typing import List

# Repositories
from src.app.expenses.domain.repositories.expense_repository import ExpenseRepository

# Entities
from src.app.expenses.domain.entities.expense import Expense

class ExpenseService:
    
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository
        
    def get_all(self, id_user: int) -> List[Expense]:
        return self.expense_repository.get_all(id_user)
    
    def get_by_id(self, id_user: int , id_expense: int) -> Expense:
        return self.expense_repository.get_by_id(id_user, id_expense)
    
    def create(self, id_user: int, expense: Expense) -> Expense:
        return self.expense_repository.create(id_user, expense)
    
    def update(self, id_user: int, id_expense: int, expense: Expense) -> Expense:
        return self.expense_repository.update(id_user, id_expense, expense)
    
    def delete(self, id_user: int, id_expense: int) -> bool:
        return self.expense_repository.delete(id_user, id_expense)