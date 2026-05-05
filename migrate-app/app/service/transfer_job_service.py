from collections import Counter, defaultdict
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.model.item_result import ItemResult
from app.model.transfer_job import TransferJob
from app.model.transfer_job_item import TransferJobItem
from app.schema.response.item_status import ItemStatus
from app.schema.response.job_summary import JobSummary

class TransferJobService:
    pg: Session
    
    def __init__(self, pg: Session):
        self.pg = pg

    @staticmethod
    def __to_summary(job: TransferJob, items: list[TransferJobItem]):
        counts = Counter(i.result for i in items)
        return JobSummary(
            job_id=job.job_id,
            status=job.status,
            pushed_at=job.pushed_at,
            completed_at=job.completed_at,
            recount={
                ItemResult.Success: counts[ItemResult.Success],
                ItemResult.Failure: counts[ItemResult.Failure],
                ItemResult.Pending: counts[ItemResult.Pending],
            },
            items=[ItemStatus(item_id=i.item_id, row_id=i.row_id, result=i.result) for i in items]
        )

    def save(self, row_ids: list[str]):
        job = TransferJob()
        self.pg.add(job)
        self.pg.flush()
        self.pg.add_all(
            [TransferJobItem(job_id=job.job_id, row_id=id) for id in row_ids]
        )
        self.pg.commit()
        return job.job_id

    def get_list(self) -> list[JobSummary]:
        jobs = self.pg.scalars(select(TransferJob)).all()
        if not jobs:
            return []
        
        stmt = select(TransferJobItem).where(TransferJobItem.job_id.in_([j.job_id for j in jobs]))
        items = self.pg.scalars(stmt).all()

        group = defaultdict(list)

        for item in items:
            group[item.job_id].append(item)

        return [self.__to_summary(j, group[j.job_id]) for j in jobs]

    def get_by_id(self, job_id: str) -> JobSummary | None:
        job = self.pg.get(TransferJob, job_id)

        if not job:
            return None
        
        stmt = select(TransferJobItem).where(TransferJobItem.job_id == job_id)
        items = self.pg.scalars(stmt).all()

        return self.__to_summary(job, list(items))