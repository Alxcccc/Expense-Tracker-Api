from pydantic import BaseModel, Field, field_validator

class ExpenseDescription(BaseModel):
    value: str = Field(..., description="Description of expense")
    
    @field_validator("value")
    def validator_description(cls, value: str, size_max = 250):
        if len(value) > size_max:
            raise ValueError(f"the length of Description is greater than {size_max}")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseDescription) and self.value == other.value
    
    def __str__(self):
        return self.value