from pydantic import BaseModel, Field, field_validator

class ExpenseTitle(BaseModel):
    value: str = Field(..., description="Title of expense")
    
    @field_validator("value")
    def validator_title(cls, value: str, size_max = 20):
        if len(value) > size_max:
            raise ValueError(f"the length of title is greater than {size_max}")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseTitle) and self.value == other.value
    
    def __str__(self):
        return self.value