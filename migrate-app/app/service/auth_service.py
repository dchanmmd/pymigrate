from datetime import datetime, timedelta, timezone
import secrets
from typing import Any
from app.model.session import Session as PySession
from sqlalchemy.orm import Session

class AuthService:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg

    def create_session(self, data: Any, ip_address: str, user_agent: str) -> str: # TODO narrow type
        pysessid = secrets.token_urlsafe(32)
        session = PySession(
            pysessid=pysessid, 
            user_id=data['user_id'], # TODO extract from payload
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=datetime.now(timezone.utc) + timedelta(days=7)
        )
        self.pg.add(session)
        self.pg.commit()

