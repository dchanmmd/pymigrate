from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.model.job_status import JobStatus
from app.model.transfer_job import TransferJob

class TransferJobRepository:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg
    
    def claim_pending(self, limit: int = 10) -> list[TransferJob]:
        stmt = (
            select(TransferJob)
            .where(TransferJob.status == JobStatus.Pending)
            .order_by(TransferJob.pushed_at)
            .with_for_update(skip_locked=True)
            .limit(limit)
        )

        jobs = self.pg.scalars(stmt).all()

        if not jobs:
            return []

        for job in jobs:
            job.status = JobStatus.Processing
            job.shifted_at = func.now()

        self.pg.commit()
        return jobs
