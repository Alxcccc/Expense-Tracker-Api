from typing import Optional, Union

# Repositories
from src.app.users.domain.repositories.user_repository import UserRepository

# Entities
from src.app.users.domain.entities.user import User, UserCreate

class UserService:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    def get_by_id(self, id_user: int) -> Optional[User]:
        return self.user_repository.get_by_id(id_user)
    
    def create(self, user: UserCreate) -> Union[User, bool]:
        return self.user_repository.create(user)
    
    def delete(self, id_user: int) -> bool:
        return self.user_repository.delete(id_user)