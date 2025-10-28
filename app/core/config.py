from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(
        alias = "DATABASE_URL"
    )

    model_config = SettingsConfigDict(
        env_file=".env.example",
        extra="ignore"
    )

    @property
    def db_url(self)->str:
        return self.database_url

settings = Settings()
