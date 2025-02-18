from fastapi import APIRouter, HTTPException, Depends
from typing_extensions import Annotated

from src.app.expenses.domain.entities.expense import Expense, ExpenseCreate
from src.app.expenses.infrastructure.repositories.expense_repository_impl import ExpenseRepositoryImpl
from src.app.expenses.application.services.expense_service import ExpenseService

# Validator
from src.app.expenses.domain.value_objects.expense_id import ExpenseId

# Auth
from src.app.users.infrastructure.routers.user_router import get_current_user

router = APIRouter()

def get_product_service():
    repository = ExpenseRepositoryImpl()
    return ExpenseService(repository)

@router.get("/", summary="Get all expenses by id_user" ,response_model=list[Expense])
def get_expenses(id_user_token: Annotated[str, Depends(get_current_user)], service: ExpenseService = Depends(get_product_service)) -> list[Expense]:
    try:
        result = service.get_all(id_user_token)
        if not result:
            raise HTTPException(404, detail="This user hasn't expenses")
        return result
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@router.get("/{id_expense}")
def get_expense(id_user_token: Annotated[str, Depends(get_current_user)], id_expense: int, service: ExpenseService = Depends(get_product_service)) -> Expense:
    try:
        validation_id_expense = ExpenseId(value=id_expense)
        result = service.get_by_id(id_user_token, validation_id_expense.value)
        if not result:
            raise HTTPException(404, detail="This expense not exists")
        return result

    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    
@router.post("/create", status_code=201)
def create_expense(id_user_token: Annotated[str, Depends(get_current_user)], expense: ExpenseCreate, service: ExpenseService = Depends(get_product_service)):
    try:
        service.create(id_user_token, expense)
        return {"message": "The expense created succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.put("/edit/{id_expense}")
def edit_expense(id_user_token: Annotated[str, Depends(get_current_user)], id_expense: int, expense: ExpenseCreate, service: ExpenseService = Depends(get_product_service)):
    try:
        service.update(id_user_token, id_expense, expense)
        return {"message": "The expense updated succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.delete("/delete/{id_expense}")
def delete_expense(id_user_token: Annotated[str, Depends(get_current_user)], id_expense: int, service: ExpenseService = Depends(get_product_service)):
    try:
        service.delete(id_user_token, id_expense)
        return {"message": "The expense deleted succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
        