from typing import Annotated, Generator

from fastapi import Depends

from app.db.postgres import Postgres
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config.settings import get_settings

settings = get_settings()

pg_engine = create_engine(settings.pg_url, future=True)
my_engine = create_engine(settings.rds_url, future=True)


def create_postgres():
    from app.model.category_map import CategoryMap
    from app.model.transfer_job import TransferJob
    from app.model.transfer_job_item import TransferJobItem

    Postgres.metadata.create_all(pg_engine)

def get_pg_session() -> Generator[Session, None, None]:
    session = Session(pg_engine)
    try: 
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_my_session() -> Generator[Session, None, None]:
    session = Session(my_engine)
    try: 
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

RequiresPostgres = Annotated[Session, Depends(get_pg_session)]
RequiresMySQL= Annotated[Session, Depends(get_my_session)]