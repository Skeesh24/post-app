from passlib.context import CryptContext


class Hasher:
    def __init__(self):
        self.__context = CryptContext(schemes=["bcrypt"])

    def get_hashed(self, plain_pass: str) -> str:
        return self.__context.hash(plain_pass)

    def verify(self, secret: str, hash: str) -> bool:
        return self.__context.verify(secret, hash)
