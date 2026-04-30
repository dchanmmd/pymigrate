from collections import defaultdict
from app.schema.itemized_job import ItemizedJob
from app.schema.job_item import JobItem
from app.model.sql.item_result import ItemResult
from app.model.sql.job_status import JobStatus
from app.model.sql.transfer_job import TransferJob
from app.model.sql.transfer_job_item import TransferJobItem
from sqlmodel import Session, and_, col, select

class JobService:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg

    def __to_itemized(self, job: TransferJob, items: list[TransferJobItem]):
        return ItemizedJob(
            id=job.job_id,
            owner_id=job.job_id,
            status=job.status,
            result=job.result,
            pushed_at=job.pushed_at,
            shifted_at=job.shifted_at,
            completed_at=job.completed_at,
            retries=job.retries,
            error=job.error,
            items=[JobItem(id=i.item_id, job_id=i.job_id, row_id=i.job_id, result=i.result) for i in items]
        )

    def get_earliest_jobs(self, count: int = 10):
        job_q = select(TransferJob).where(TransferJob.status == JobStatus.Pending).order_by(col(TransferJob.pushed_at).asc()).limit(count)
        jobs = self.pg.exec(job_q).all()
        job_ids = [j.job_id for j in jobs]
        job_item_q = select(TransferJobItem).where(and_(TransferJobItem.result == ItemResult.Pending, col(TransferJobItem.job_id).in_(job_ids)))
        job_items = self.pg.exec(job_item_q).all()
        rows = defaultdict(list)
        for item in job_items:
            rows[item.job_id].append(item)
        return [self.__to_itemized(job, rows[job.job_id]) for job in jobs]
        