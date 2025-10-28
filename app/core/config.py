from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class DBSettings(BaseSettings):
    url: str = Field(alias="DATABASE_URL", default="postgresql+asyncpg://user:password@localhost:5432/name")

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env.example",
        extra="ignore"
    )
    db: DBSettings = DBSettings()
settings = Settings()
