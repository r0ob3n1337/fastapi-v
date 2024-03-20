from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Файл настроек для работы с env переменными"""

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    class Config:
        """Внутренний класс, который подскажет pydantic где искать"""

        env_file = ".env"


settings = Settings()
