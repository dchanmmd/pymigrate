from typing import Annotated

from app.db.session import RequiresPostgres
from app.schema.response.item_response import ItemResponse
from app.schema.response.list_response import ListResponse
from app.schema.response.job_summary import JobSummary
from app.error.failed_operation_error import FailedOperationError
from app.error.not_found_error import NotFoundError
from app.service.transfer_service import TransferService
from app.schema.request.transfer_request import TransferRequest
from fastapi import APIRouter, Depends, HTTPException

def __get_service(pg: RequiresPostgres):
    return TransferService(pg)

RequiresTransferService = Annotated[TransferService, Depends(__get_service)]

router = APIRouter(prefix='/transfers')

@router.post('/', status_code=202, response_model=ItemResponse[str])
def create_transfer_job(data: TransferRequest, service: RequiresTransferService):
    try: 
        job_id = service.save_job(data.row_ids)
        return ItemResponse[str](success=True, message='El trabajo fue creado exitosamente.', data=job_id)
    except RuntimeError as e:
        raise HTTPException(500, detail=str(e))
    
@router.get('/', response_model=ListResponse[JobSummary])
def check_job_list(service: RequiresTransferService):
    try: 
        jobs = service.get_job_list('') # TODO autenticación
        return ListResponse(success=True, message='Se obtuvieron los reportes con éxito.', data=jobs)
    except RuntimeError as e:
        raise HTTPException(500, detail=str(e))

@router.get('/{job_id}/status', response_model=ItemResponse[JobSummary])
def check_job_status(job_id: str, service: RequiresTransferService):
    try: 
        summary = service.get_job_summary(job_id)
        return ItemResponse(success=True, message='Se obtuvo el reporte del trabajo con éxito.', data=summary)
    except NotFoundError as e:
        raise HTTPException(404, detail=str(e))
    except FailedOperationError as e:
        raise HTTPException(500, detail=str(e))