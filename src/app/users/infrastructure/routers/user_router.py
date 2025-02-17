from fastapi import APIRouter, HTTPException, Depends

# Entities
from src.app.users.domain.entities.user import User, UserCreate

# Repositories
from src.app.users.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

# Services
from src.app.users.application.services.user_service import UserService

# Validator
from src.app.users.domain.value_objects.user_id import UserId


router = APIRouter()

def get_product_service():
    repository = UserRepositoryImpl()
    return UserService(repository)

@router.get("/{id_user}")
def get_id_user(id_user: int, service: UserService = Depends(get_product_service)) -> User:
    try:
        format_id_user = UserId(value=id_user)
        result = service.get_by_id(format_id_user.value)
        if not result:
            raise HTTPException(404, detail="User not exists")
        return result
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.post("/register")
def create_user(new_user: UserCreate, service: UserService = Depends(get_product_service)):
    try:
        service.create(new_user)
        return {"message": "The user created succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    
@router.delete("/delete/{id_user}")
def delete_expense(id_user: int, service: UserService = Depends(get_product_service)):
    try:
        service.delete(id_user)
        return {"message": "The expense deleted succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))