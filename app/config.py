from typing import Optional

from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_URL: Optional[str] = Field(default=None)
    SECRET_KEY: str
    ENCODE_ALGORITHM: str
    ADMIN_CREATE_PATH: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    @field_validator("DB_URL", mode="before")
    @classmethod
    def assemble_db_url(cls, v: Optional[str], values: ValidationInfo) -> str:
        if v is None:
            return (
                f"postgresql+asyncpg://{values.data['DB_USER']}:"
                f"{values.data['DB_PASSWORD']}@{values.data['DB_HOST']}:"
                f"{values.data['DB_PORT']}/{values.data['DB_NAME']}"
            )
        return v

    class Config:
        env_file = ".env"


settings = Settings()
