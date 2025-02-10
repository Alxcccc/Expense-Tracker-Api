from pydantic import BaseModel, Field, field_validator
from datetime import date

class ExpenseDate(BaseModel):
    value: date = Field(..., description="Date of expense")
    
    @field_validator("value")
    def validator_date(cls, value: str, format = "%Y-%m-%d"):
        if not isinstance(value, date):
            raise ValueError(f"time data {value} does not match format {format}")
        return value
        
    def __eq__(self, other):
        return isinstance(other, ExpenseDate) and self.value == other.value
    
    def __str__(self):
        return self.value