from fastapi import APIRouter, Depends

from src.app.infrastructure.database.models.expense_model import ExpenseDatabase
from src.app.expenses.infrastructure.repositories.expense_repository_impl import ExpenseRepositoryImpl
from src.app.expenses.application.services.expense_service import ExpenseService

router = APIRouter()

def get_product_service():
    repository = ExpenseRepositoryImpl()
    return ExpenseService(repository)

@router.get("/")
def get_expenses(service: ExpenseService = Depends(get_product_service)) -> list[ExpenseDatabase]:
    result = service.get_all()
    return result