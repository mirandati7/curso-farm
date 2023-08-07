from fastapi import APIRouter, Depends, status

from schemas.common_schema import CommonSchema
from schemas.user_schema import UserSchema, UserSchemaBase
from services.user_service import autenticar, inserir

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommonSchema)
async def post_product(user: UserSchema):
    inserir(user=user)
    return CommonSchema(title="Sistema", message="Salvo com sucesso",type= "toast")


@router.post('/login', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def autenticar_login(user: UserSchema):
    return autenticar(user=user)
    