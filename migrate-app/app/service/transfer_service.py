from collections import Counter
from uuid import uuid4
from sqlmodel import Session, select

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

    def get_job_summary(self, job_id: str):
        try:
            job = self.pg.get(TransferJob, job_id)
            query = select(TransferJobItem).where(TransferJobItem.job_id == job_id)
            job_items = self.pg.exec(query).all()
        except Exception as e:
            raise FailedOperationError(
                f"Ocurrió un error desconocido en el servidor.", str(e)
            )
        else:
            if job is None:
                raise NotFoundError(f"El trabajo con id '{job_id}' no fue encontrado.")

            counts = Counter(i.result for i in job_items)
            response = JobSummary(
                job_id=job.job_id,
                status=job.status,
                completed_at=job.completed_at,
                recount={
                    ItemResult.Success: counts[ItemResult.Success],
                    ItemResult.Failure: counts[ItemResult.Failure],
                    ItemResult.Pending: counts[ItemResult.Pending],
                },
                items=[ItemStatus(item_id=i.item_id, row_id=i.row_id, result=i.result) for i in job_items],
            )

            return response
