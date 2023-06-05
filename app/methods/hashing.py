from passlib.context import CryptContext


class Hashed:
    def __init__(self):
        self.__context = CryptContext(schemes=["bcrypt"])

    def get_hashed(self, secret: str) -> str:
        return self.__context.hash(secret)

    def compare_with(self, comparing_secret: str) -> bool:
        return self.__context.hash(comparing_secret) == self.__secret
