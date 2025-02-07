from pydantic import BaseModel, Field, field_validator
from datetime import date

class ExpenseDate(BaseModel):
    value: str = Field(..., description="Date of expense")
    
    @field_validator("value")
    def validator_date(cls, value: str, format = "%Y-%m-%d"):
        if not date.strftime(value, format):
            raise ValueError("The date of expense not have correct format")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseDate) and self.value == other.value
    
    def __str__(self):
        return self.value