from collections import defaultdict

from app.model.transfer_job import TransferJob
from app.model.transfer_job_item import TransferJobItem
from sqlmodel import Session, col, select

class JobService:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg

    def get_earliest_jobs(self, count: int):
        job_q = select(TransferJob).order_by(col(TransferJob.pushed_at).asc()).limit(count)
        jobs = self.pg.exec(job_q).all()
        job_ids = [j.job_id for j in jobs]
        job_item_q = select(TransferJobItem).where(col(TransferJobItem.job_id).in_(job_ids))
        job_items = self.pg.exec(job_item_q).all()
        rows = defaultdict(list)
        for item in job_items:
            rows[item.job_id].append(item)