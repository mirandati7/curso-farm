from bson import errors as beeros
from bson.objectid import ObjectId
from pymongo import errors

from core.conexao import conectar, desconectar
from schemas.product_schema import ProductSchema, ProductSchemaBase


def inserir(product: ProductSchema):
    conn = conectar()
    db = conn.farm

    nome = product.nome
    preco =  product.preco
    estoque = product.estoque

    try:
        db.produtos.insert_one(
            {
                "nome": nome,
                "preco": preco,
                "estoque": estoque
            }
        )
        print(f'O produto {nome} foi inserido com sucesso')
    except errors.PyMongoError as e:
        print(f'Não foi possível inserir o produto. {e}')
    desconectar(conn)


def consultar_por_id(id):
    conn  = conectar()
    db =  conn.farm

    _id = str(id)
    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.find_one(
                { "_id": ObjectId(_id)  },
            )            
            nome= res['nome']
            preco= res['preco']
            estoque= res["estoque"]
            desconectar(conn)
            return ProductSchema(nome=nome, preco=preco,estoque=estoque )
    except errors.PyMongoError as e:
        print(f'Erro ao acessar a base de dados: {e}')
    except beeros.InvalidId as f:
        print(f'Objeto ID invalido: {f}')
   
    

def atualizar(id: str, product: ProductSchema):
    conn  = conectar()
    db =  conn.farm

    _id = str(id)

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.update_one(
                { "_id": ObjectId(_id)  },
                {
                    "$set":  
                            {
                                "nome": product.nome,
                                "preco": product.preco,
                                "estoque": product.estoque
                            }
                }

            )

            if res.modified_count > 0:
                print(f"Produto foi alterado com sucesso")
                return ProductSchemaBase(id=str(ObjectId(_id)), nome=product.nome,preco=product.preco,estoque=product.estoque)
    except errors.PyMongoError as e:
        print(f'Erro ao acessar a base de dados: {e}')
    except beeros.InvalidId as f:
        print(f'Objeto ID invalido: {f}')
    desconectar(conn)       





def deletar():
    conn  = conectar()
    db =  conn.farm
    
    _id = input("Informe o ID do produto:")

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.delete_one(
                {
                    "_id": ObjectId(_id)
                }
            )

            if res.deleted_count > 0:
                print("Produto deletado com sucesso")
            else:
                print("Não foi deletar o produto")

    except errors.PyMongoError as e:
        print(f'Erro ao acessar a base de dados: {e}')
    except beeros.InvalidId as f:
        print(f'Objeto ID invalido: {f}')
    desconectar(conn)       

def listar():
    conn = conectar()
    db = conn.farm

    try:
        if db.produtos.count_documents({}) > 0:
            produtos = db.produtos.find()
            print('Listando os produtos')
            print('------------------')
            lst_produtos = []
            
            for item in produtos:
                product = ProductSchemaBase(id=str(item["_id"]), nome=item["nome"],preco=item["preco"],estoque=item["estoque"])
                lst_produtos.append(product)
            return lst_produtos
        else:
            print('Não existem produtos cadastrados') 

    except errors.PyMongoError as e:
        print(f'Não foi possível conectar a base de dados')
    desconectar(conn)


