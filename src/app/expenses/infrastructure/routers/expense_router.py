from fastapi import APIRouter, HTTPException,Depends

from src.app.expenses.domain.entities.expense import Expense, ExpenseCreate
from src.app.infrastructure.database.models.expense_model import ExpenseDatabase
from src.app.expenses.infrastructure.repositories.expense_repository_impl import ExpenseRepositoryImpl
from src.app.expenses.application.services.expense_service import ExpenseService

# Validator
from src.app.expenses.domain.value_objects.expense_id_user import ExpenseIdUser
from src.app.expenses.domain.value_objects.expense_id import ExpenseId

router = APIRouter()

def get_product_service():
    repository = ExpenseRepositoryImpl()
    return ExpenseService(repository)

@router.get("/{id_user}", summary="Get all expenses by id_user" ,response_model=list[Expense])
def get_expenses(id_user: int, service: ExpenseService = Depends(get_product_service)) -> list[Expense]:
    try:
        validation_id_user = ExpenseIdUser(value=id_user)
        result = service.get_all(validation_id_user.value)
        if not result:
            raise HTTPException(404, detail="This user hasn't expenses")
        return result
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@router.get("/{id_user}/{id_expense}")
def get_expense(id_user: int, id_expense: int, service: ExpenseService = Depends(get_product_service)) -> Expense:
    try:
        validation_id_user = ExpenseIdUser(value=id_user)
        validation_id_expense = ExpenseId(value=id_expense)
        result = service.get_by_id(validation_id_user.value, validation_id_expense.value)
        if not result:
            raise HTTPException(404, detail="This expense not exists")
        return result

    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    
@router.post("/{id_user}/create", status_code=201)
def create_expense(id_user: int, expense: ExpenseCreate, service: ExpenseService = Depends(get_product_service)):
    try:
        service.create(id_user, expense)
        return {"message": "The expense created succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.put("/{id_user}/edit/{id_expense}")
def edit_expense(id_user: int, id_expense: int, expense: ExpenseCreate, service: ExpenseService = Depends(get_product_service)):
    try:
        service.update(id_user, id_expense, expense)
        return {"message": "The expense updated succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.delete("/{id_user}/delete/{id_expense}")
def delete_expense(id_user: int, id_expense: int, service: ExpenseService = Depends(get_product_service)):
    try:
        service.delete(id_user, id_expense)
        return {"message": "The expense deleted succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
        