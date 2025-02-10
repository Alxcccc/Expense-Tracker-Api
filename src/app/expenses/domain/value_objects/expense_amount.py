from pydantic import BaseModel, Field, field_validator

class ExpenseAmount(BaseModel):
    value: int = Field(..., description="Date of expense")
    
    @field_validator("value")
    def validator_amount(cls, value: int):
        if value <= 0:
            raise ValueError("This price is zero or less than zero")
        return value
        
    def __eq__(self, other):
        return isinstance(other, ExpenseAmount) and self.value == other.value
    
    def __str__(self):
        return self.value