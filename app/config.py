from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_DRIVER: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORYTHM: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"


Config = Settings()
