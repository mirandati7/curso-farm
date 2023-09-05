from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from core.auth import criar_token_acesso
from core.deps import get_current_user
from schemas.common_schema import CommonSchema
from schemas.user_schema import UserSchema, UserSchemaBase
from services.user_service import autenticar, inserir

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommonSchema)
async def post_product(user: UserSchema, user_logged:any = Depends(get_current_user)):
    inserir(user=user)
    return CommonSchema(title="Sistema", message="Salvo com sucesso",type= "toast")


@router.post('/login', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def autenticar_login(user: UserSchema):
    user = autenticar(user=user)
    if user != None:
        print( user.id)
        print("Geracao de token JWT")
        print(criar_token_acesso(sub=user.id))
        return JSONResponse(content={"access_token": criar_token_acesso(sub=user.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
    else:
        return UserSchemaBase(login="Usuario não logado")

    