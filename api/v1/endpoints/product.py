from typing import List

from fastapi import APIRouter, Depends, status

from core.deps import get_current_user
from schemas.common_schema import CommonSchema
from schemas.product_schema import ProductSchema, ProductSchemaBase
from services.product_service import (atualizar, consultar_por_id, inserir,
                                      listar)

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommonSchema)
async def post_product(product: ProductSchema,user_logged:any = Depends(get_current_user)):
    inserir(product=product)
    return CommonSchema(title="Sistema", message="Salvo com sucesso",type= "toast")


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductSchema)
async def get_product(id: str,user_logged:any = Depends(get_current_user) ):
    return consultar_por_id(id=id)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductSchemaBase])
async def get_product_list(user_logged:any = Depends(get_current_user)):
    return listar()

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=ProductSchemaBase)
async def put_product(_id: str,product: ProductSchema,user_logged:any = Depends(get_current_user)):
    return atualizar(id=_id, product=product)