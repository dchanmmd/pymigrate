from datetime import datetime, timezone
from sqlalchemy import DateTime, Index, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.postgres import Postgres

class Session(Postgres):
    __tablename__ = 'sessions'
    __table_args__ = (Index('idx_uid_ip_ua', 'user_id', 'ip_address', 'user_agent'),)

    pysessid: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    user_agent: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default_factory= lambda: datetime.now(timezone.utc))
    expires_at: Mapped[datetime] = mapped_column(DateTime)