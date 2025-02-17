from pydantic import BaseModel, Field, field_validator, validate_email
from email_validator import EmailNotValidError

class UserGmail(BaseModel):
    value: str = Field(..., description="Gmail of user")
    
    @field_validator("value")
    def validator_gmail(cls, value: str):
        try:
            validate = validate_email(value)
            return validate[1]
        
        except EmailNotValidError as e:
            raise ValueError(str(e))
        
    
    def __eq__(self, other):
        return isinstance(other, UserGmail) and self.value == other.value
    
    def __str__(self):
        return self.value