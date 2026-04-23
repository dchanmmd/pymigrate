from app.schema.request.login_request import LoginRequest
from fastapi import APIRouter

router = APIRouter(prefix='/auth')

@router.post('/login')
def authenticate_user(data: LoginRequest):
    print(data.__dict__) # TODO Call mmdpawn API