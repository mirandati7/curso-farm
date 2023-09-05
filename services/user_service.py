from bson import errors as beeros
from bson.objectid import ObjectId
from pymongo import errors

from core.conexao import conectar, desconectar
from core.security import generate_hash_password, verify_password
from schemas.user_schema import UserSchema, UserSchemaBase


def inserir(user: UserSchema):
    conn = conectar()
    db = conn.farm

    login    = user.login
    password =  generate_hash_password(user.password)
    
    try:
        db.users.insert_one(
            {
                "login": login,
                "password": password
            }
        )
        print(f'O usuario {login} foi inserido com sucesso')
    except errors.PyMongoError as e:
        print(f'Não foi possível inserir o usuario. {e}')
    desconectar(conn)


def autenticar(user: UserSchema):
    conn = conectar()
    db =  conn.farm

    login    = user.login
    password =  user.password

    try:
        if db.users.count_documents({}) > 0:
            res = db.users.find_one(
                {"login": login }
            )
            if res != None:
                login= res['login']
                password = res['password']
                id = res['_id']

                print(f"id do mongo:  {id}" )

                if not verify_password(user.password, password):
                    print(f"senhas diferentes {password}" )
                    desconectar(conn)
                    return None
                else:
                    desconectar(conn)
                    return UserSchemaBase(id=str(id),login=login)

    except errors.PyMongoError as e:
        print(f'Erro ao acessar a base de dados: {e}' )