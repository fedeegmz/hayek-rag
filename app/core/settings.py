from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    mongodb_uri: str = Field(...)
    db_name: str = Field(...)
    embedding_api_key: str = Field(...)
    gemini_api_key: str = Field(...)


settings = Settings()
