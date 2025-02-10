from pydantic import BaseModel, Field, field_validator

class ExpenseId(BaseModel):
    value: int = Field(..., description="Id of expense")
    
    @field_validator("value")
    def validator_id(cls, value: int):
        if value <= 0:
            raise ValueError("This id is zero or less than zero")
        return value
        
    def __eq__(self, other):
        return isinstance(other, ExpenseId) and self.value == other.value
    
    def __str__(self):
        return self.value