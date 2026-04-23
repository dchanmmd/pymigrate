from app.schema.response.job_status_response import JobStatusResponse
from app.error.failed_operation_error import FailedOperationError
from app.error.not_found_error import NotFoundError
from app.service.transfer_service import save_job, get_job_summary
from app.schema.request.transfer_request import TransferRequest
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/transfers')

@router.post('/', status_code=202)
def create_transfer_job(data: TransferRequest):
    try: 
        print(data.__dict__)
        save_job(data.row_ids)
    except FailedOperationError as e:
        raise HTTPException(500, detail=str(e))

@router.get('/{job_id}/status', response_model=JobStatusResponse)
def check_job_status(job_id: str):
    try: 
        summary = get_job_summary(job_id)
        return summary
    except NotFoundError as e:
        raise HTTPException(404, detail=str(e))
    except FailedOperationError as e:
        raise HTTPException(500, detail=str(e))