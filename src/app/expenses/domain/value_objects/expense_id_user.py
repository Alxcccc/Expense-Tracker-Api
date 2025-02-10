from pydantic import BaseModel, Field, field_validator

class ExpenseIdUser(BaseModel):
    value: int = Field(..., description="Id of expense's owner")
    
    @field_validator("value")
    def validator_id_user(cls, value: int):
        if value <= 0:
            raise ValueError("This id is zero or less than zero")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseIdUser) and self.value == other.value
    
    def __str__(self):
        return self.value