from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    pool_size: int
    max_overflow: int


class Settings(BaseSettings):
    db: DatabaseConfig
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="MAIN__",
    )
    

settings = Settings()