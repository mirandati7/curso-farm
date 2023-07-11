from fastapi import APIRouter, Depends, status

from schemas.common_schema import CommonSchema
from schemas.product_schema import ProductSchema
from services.produto import consultar_por_id, inserir

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommonSchema)
async def post_product(product: ProductSchema):
    inserir(product=product)
    return CommonSchema(title="Sistema", message="Salvo com sucesso",type= "toast")


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductSchema)
async def get_product(id: str):
    return consultar_por_id(id=id)