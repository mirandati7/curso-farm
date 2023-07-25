from typing import Optional

from pydantic import BaseModel as SCBaseModel


class ProductSchema(SCBaseModel):
    nome:str
    preco: float
    estoque: float
    
    class Config:
        orm_mode = True

class ProductSchemaBase(SCBaseModel):
    id: str
    nome:str
    preco: float
    estoque: float
    
    class Config:
        orm_mode = True