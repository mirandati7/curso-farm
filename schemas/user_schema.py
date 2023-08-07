from typing import Optional

from pydantic import BaseModel as SCBaseModel


class UserSchema(SCBaseModel):
    login:str
    password: str
        
    class Config:
        orm_mode = True

class UserSchemaBase(SCBaseModel):
    id: Optional[str] = None
    login:str    
    
    class Config:
        orm_mode = True