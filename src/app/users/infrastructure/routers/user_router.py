from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated, Union
import jwt

# Entities
from src.app.users.domain.entities.user import User, UserCreate

# Repositories
from src.app.users.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

# Services
from src.app.users.application.services.user_service import UserService

# Validator
from src.app.users.domain.value_objects.user_id import UserId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")

router = APIRouter()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    id_user = payload.get("sub")
    return id_user

def get_product_service():
    repository = UserRepositoryImpl()
    return UserService(repository)

@router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], service: UserService = Depends(get_product_service)):
    try:
        username, password = form_data.username, form_data.password
        result = service.login(username, password)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": str(result)}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    
    except ValueError as e:
        raise HTTPException(500, detail=str(e))
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    

@router.get("/")
def get_id_user(id_user_token: Annotated[str, Depends(get_current_user)], service: UserService = Depends(get_product_service)) -> User:
    try:
        format_id_user = UserId(value=int(id_user_token))
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
def delete_user(id_user_token: Annotated[str, Depends(get_current_user)], id_user: int, service: UserService = Depends(get_product_service)):
    try:
        service.delete(id_user)
        return {"message": "The expense deleted succesfully"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))