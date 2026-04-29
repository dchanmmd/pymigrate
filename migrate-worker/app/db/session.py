from app.config.app_environment import env
from sqlmodel import Session, create_engine
from sqlalchemy import Engine

def _make_engine(url: str) -> Engine:
    return create_engine(
        url,
        pool_size=5,          
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=1800,
    )

pg_engine  = _make_engine(env.pg_url)
rds_engine = _make_engine(env.rds_url)


def get_pg_session():
    with Session(pg_engine) as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise


def get_rds_session():
    with Session(rds_engine) as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise