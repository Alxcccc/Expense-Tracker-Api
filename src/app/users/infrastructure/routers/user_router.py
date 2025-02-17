from fastapi import APIRouter, HTTPException, Depends

# Entities
from src.app.users.domain.entities.user import User, UserCreate

# Repositories
from src.app.users.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

# Services
from src.app.users.application.services.user_service import UserService

# Database
from src.app.infrastructure.database.database import DataBase

# Models Database
from src.app.infrastructure.database.models.user_model import UserDatabase

# Validator
from src.app.users.domain.value_objects.user_id import UserId
from src.app.users.domain.value_objects.user_username import UserUsername
from src.app.users.domain.value_objects.user_password import UserPassword
from src.app.users.domain.value_objects.user_email import UserGmail

router = APIRouter()

def get_product_service():
    repository = UserRepositoryImpl()
    return UserService(repository)

@router.get("/{id_user}")
def get_id_user(id_user: int, service: UserService = Depends(get_product_service)):
    try:
        format_id_user = UserId(value=id_user)
        result = service.get_by_id(format_id_user.value)
        if not result:
            raise HTTPException(404, detail="User not exists")
        return result
    except Exception as e:
        raise HTTPException(404, detail=str(e))