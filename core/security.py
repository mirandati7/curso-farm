from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def generate_hash_password(password: str) -> str:
    """"
       Função que gera e retorna o hash da senha
    """
    return CRIPTO.hash(password)


def verify_password(password: str, hash_password: str) -> bool:
    return CRIPTO.verify(password, hash_password)
