from pymongo import MongoClient, errors


# metodo para conectar no mongodb
def conectar():
    conn = MongoClient(host="localhost", port=27017)
    return conn

# metodo para descconectar do mongodb
def desconectar(conn):
    if conn:
        conn.close()
