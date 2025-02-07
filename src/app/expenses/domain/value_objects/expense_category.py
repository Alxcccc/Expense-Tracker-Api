from pydantic import BaseModel, Field, field_validator

class ExpenseCategory(BaseModel):
    value: str = Field(..., description="Description of expense")
    
    @field_validator("value")
    def validator_description(cls, value: str, categories = ["groceries", "leisure", "electronics", "utilities", "clothing", "health", "others"]):
        if not value.lower() in categories:
            raise ValueError(f"it isn't a correct category")
        
    def __eq__(self, other):
        return isinstance(other, ExpenseCategory) and self.value == other.value
    
    def __str__(self):
        return self.value