from pydantic import BaseModel, Field, field_validator

class UserUsername(BaseModel):
    value: str = Field(..., description="Username")
    
    @field_validator("value")
    def validator_username(cls, value: str, size_max = 20):
        
        if len(value) > size_max:
            raise ValueError(f"the length of username is greater than {size_max}")
        
        return value
    
    def __eq__(self, other):
        return isinstance(other, UserUsername) and self.value == other.value
    
    def __str__(self):
        return self.value