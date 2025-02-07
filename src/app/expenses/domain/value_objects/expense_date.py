from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class ExpenseDate(BaseModel):
    value: str = Field(..., description="Date of expense")
    
    @field_validator("value")
    def validator_date(cls, value: str, format = "%Y-%m-%d"):
        try:
            datetime.strptime(value, format)
        except ValueError:
            raise ValueError(f"time data {value} does not match format {format}")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseDate) and self.value == other.value
    
    def __str__(self):
        return self.value