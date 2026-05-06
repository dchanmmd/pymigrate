from typing import Annotated

from app.db.session import RequiresPostgres
from app.schema.response.item_response import ItemResponse
from app.schema.response.list_response import ListResponse
from app.schema.response.job_summary import JobSummary
from app.error.failed_operation_error import FailedOperationError
from app.error.not_found_error import NotFoundError
from app.service.transfer_job_service import TransferJobService
from app.schema.request.transfer_request import TransferRequest
from fastapi import APIRouter, Depends, HTTPException

def __get_service(pg: RequiresPostgres):
    return TransferJobService(pg)

RequiresTransferService = Annotated[TransferJobService, Depends(__get_service)]

router = APIRouter(prefix='/transfers')

@router.get('/', response_model=ListResponse[JobSummary])
def check_job_list(service: RequiresTransferService):
    job_list = service.get_list()
    if not job_list:
        raise HTTPException(404, 'No se encontraron los trabajos.')
    return ListResponse(success=True, message='Se obtuvo el reporte del trabajo con éxito.', data=job_list)

@router.post('/', status_code=202, response_model=ItemResponse[str])
def create_transfer_job(data: TransferRequest, service: RequiresTransferService):
    job_id = service.save(data.row_ids)
    return ItemResponse[str](success=True, message="El trabajo fue creado exitosamente.", data=job_id)

@router.get('/{job_id}', response_model=ItemResponse[JobSummary])
def check_job_status(job_id: str, service: RequiresTransferService):
    summary = service.get_by_id(job_id)
    if summary is None:
        raise HTTPException(404, 'No se encontró este trabajo.')
    return ItemResponse(success=True, message='Se obtuvo el reporte del trabajo con éxito.', data=summary)