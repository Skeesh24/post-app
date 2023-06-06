from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_DRIVER: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"


Config = Settings()
