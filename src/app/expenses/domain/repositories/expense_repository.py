from abc import ABC, abstractmethod
from typing import List, Optional, Union

from src.app.expenses.domain.entities.expense import Expense

class ExpenseRepository(ABC):
    
    @abstractmethod
    def get_all(self, id_user: int) -> List[Expense]:
        pass
    
    @abstractmethod
    def get_by_id(self, id_user: int, id_expense: int) -> Optional[Expense]:
        pass
    
    @abstractmethod
    def create(self, id_user, expense: Expense) -> Expense:
        pass
    
    @abstractmethod
    def update(self, id_user: int, id_expense: int, expense: Expense) -> Union[bool, Expense]:
        pass
    
    @abstractmethod
    def delete(self, id_user: int, id_expense: int) -> bool:
        pass