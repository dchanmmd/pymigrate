from app.config.environment import Environment

class AppEnvironment(Environment):
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

    @property
    def pg_url(self):
        return f"{self.PG_DRIVER}://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"
    
    @property
    def rds_url(self):
        return f"{self.RDS_DRIVER}://{self.RDS_USER}:{self.RDS_PASSWORD}@{self.RDS_HOST}:{self.RDS_PORT}/{self.RDS_NAME}"

env = AppEnvironment()