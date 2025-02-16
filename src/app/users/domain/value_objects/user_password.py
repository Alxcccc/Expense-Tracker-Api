from pydantic import BaseModel, Field, field_validator

class UserPassword(BaseModel):
    value: str = Field(..., description="Password of user")
    
    @field_validator("value")
    def validator_password(cls, value: str, size_max = 20):
        
        if len(value) > size_max:
            raise ValueError(f"the length of password is greater than {size_max}")
        
        return value
    
    def __eq__(self, other):
        return isinstance(other, UserPassword) and self.value == other.value
    
    def __str__(self):
        return self.value