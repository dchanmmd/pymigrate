import logging
from app.error.failed_operation_error import FailedOperationError
from app.error.not_found_error import NotFoundError
from app.schema.response.job_status_response import JobStatusResponse
from app.schema.response.item_status import ItemStatus
from app.db.session import RequiresPostgres
from app.model.transfer_job import TransferJob
from app.model.transfer_job_item import TransferJobItem
from sqlmodel import select

logger = logging.getLogger(__name__)

def save_job(row_ids: list[str], session: RequiresPostgres):
    pass

def get_job_summary(job_id: str, session: RequiresPostgres):
    try:
        job = session.get(TransferJob, job_id)
        query = select(TransferJobItem).where(TransferJobItem.job_id == job_id)
        job_items = session.exec(query).all()
    except Exception as e:
        logger.error(f"An unknown error occurred while retrieving job data from the database.\n{e}")
        raise FailedOperationError(f"Ocurrió un error desconocido en el servidor.")
    else:
        if job is None:
            logger.error(f"Attempted to retrieve a job with id '{job_id}' but got None.")
            raise NotFoundError(f"El trabajo con id '{job_id}' no fue encontrado.")
        response = JobStatusResponse()
        response.job_id = job.job_id
        response.status = job.status
        response.completed_at = job.completed_at
        response.items = [ItemStatus(i.item_id, i.row_id, i.result) for i in job_items]