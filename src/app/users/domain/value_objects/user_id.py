from pydantic import BaseModel, Field, field_validator

class UserId(BaseModel):
    value: int = Field(..., description="Id user")
    
    @field_validator("value")
    def validator_id(cls, value: int):
        if value <= 0:
            raise ValueError("This id is zero or less than zero")
        return value
        
    def __eq__(self, other):
        return isinstance(other, UserId) and self.value == other.value
    
    def __str__(self):
        return self.value
        
        