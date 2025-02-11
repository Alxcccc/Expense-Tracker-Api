from abc import ABC, abstractmethod
from typing import Optional, Union

# entities
from src.app.users.domain.entities.user import User, UserCreate

class UsersRepository(ABC):

    @abstractmethod
    def get_by_id(self, id_user: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def create(self, user: UserCreate) -> Union[User, bool]:
        pass
    
    @abstractmethod
    def delete(self, id_user: int) -> bool:
        pass