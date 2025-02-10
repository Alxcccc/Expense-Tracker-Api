from fastapi import APIRouter, HTTPException,Depends

from src.app.expenses.domain.entities.expense import Expense
from src.app.infrastructure.database.models.expense_model import ExpenseDatabase
from src.app.expenses.infrastructure.repositories.expense_repository_impl import ExpenseRepositoryImpl
from src.app.expenses.application.services.expense_service import ExpenseService

# Validator
from src.app.expenses.domain.value_objects.expense_id_user import ExpenseIdUser

router = APIRouter()

def get_product_service():
    repository = ExpenseRepositoryImpl()
    return ExpenseService(repository)

@router.get("/{id_user}/expenses")
def get_expenses(id_user: int, service: ExpenseService = Depends(get_product_service)):
    try:
        validation_id_user = ExpenseIdUser(value=id_user)
        result = service.get_all(validation_id_user.value)
        return result
    except ValueError as e:
        raise HTTPException(400, detail=str(e))