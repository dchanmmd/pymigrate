from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    RDS_DRIVER: str
    RDS_HOST: str
    RDS_PORT: int
    RDS_USER: str
    RDS_PASSWORD: str
    RDS_NAME: str

    PG_DRIVER: str
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_NAME: str

    JWT_ACCESS_SECRET: str
    JWT_REFRESH_SECRET: str

    @computed_field
    @property
    def pg_url(self) -> str:
        return URL.create(
            drivername=self.PG_DRIVER,
            username=self.PG_USER,
            password=self.PG_PASSWORD,
            host=self.PG_HOST,
            port=self.PG_PORT,
            database=self.PG_NAME,
        )
    
    @computed_field
    @property
    def rds_url(self) -> str:
        return URL.create(
            drivername=self.RDS_DRIVER,
            username=self.RDS_USER,
            password=self.RDS_PASSWORD,
            host=self.RDS_HOST,
            port=self.RDS_PORT,
            database=self.RDS_NAME,
        )
    
@lru_cache
def get_settings() -> Settings:
    return Settings()