from collections import Counter, defaultdict
from sqlmodel import Session, col, select
from app.error.failed_operation_error import FailedOperationError
from app.error.not_found_error import NotFoundError
from app.model.item_result import ItemResult
from app.model.transfer_job import TransferJob
from app.model.transfer_job_item import TransferJobItem
from app.schema.response.item_status import ItemStatus
from app.schema.response.job_summary import JobSummary


class TransferService:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg

    def save_job(self, row_ids: list[str]):
        job = TransferJob()
        self.pg.add(job)
        self.pg.flush()
        self.pg.add_all(
            [TransferJobItem(job_id=job.job_id, row_id=id) for id in row_ids]
        )
        self.pg.commit()
        return job.job_id
    
    def __to_summary(self, job: TransferJob, items: list[TransferJobItem]) -> JobSummary:
        counts = Counter(i.result for i in items)
        return JobSummary(
            job_id=job.job_id,
            pushed_at=job.pushed_at,
            status=job.status,
            completed_at=job.completed_at,
            recount={
                ItemResult.Success: counts[ItemResult.Success],
                ItemResult.Failure: counts[ItemResult.Failure],
                ItemResult.Pending: counts[ItemResult.Pending],
            },
            items=[ItemStatus(item_id=i.item_id, row_id=i.row_id, result=i.result) for i in items],
        )
    
    def get_job_list(self, user_id: str) -> list[JobSummary]:
        try:
            query = select(TransferJob) # .where(TransferJob.owner_id == user_id) # TODO autenticación 
            result = self.pg.exec(query).all()

            if result is None or not len(result):
                return []
            
            job_ids = [j.job_id for j in result]
            subq = select(TransferJobItem).where(col(TransferJobItem.job_id).in_(job_ids))
            
            items = self.pg.exec(subq).all()
            items_by_job = defaultdict(list)

            for item in items:
                items_by_job[item.job_id].append(item)
            return [self.__to_summary(job=j, items=items_by_job[j.job_id]) for j in result]
        except Exception as e:
            raise FailedOperationError(
                f"Ocurrió un error desconocido en el servidor.", str(e)
            )


    def get_job_summary(self, job_id: str):
        try:
            job = self.pg.get(TransferJob, job_id)
            if job is None:
                raise NotFoundError(f"El trabajo con id '{job_id}' no fue encontrado.")
    
            query = select(TransferJobItem).where(TransferJobItem.job_id == job_id)
            job_items = self.pg.exec(query).all()
        except NotFoundError:
            raise
        except Exception as e:
            raise FailedOperationError(
                f"Ocurrió un error desconocido en el servidor.", str(e)
            )
        else:
            return self.__to_summary(job=job, items=list(job_items))
