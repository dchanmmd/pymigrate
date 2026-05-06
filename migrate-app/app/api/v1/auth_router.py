from app.schema.request.login_request import LoginRequest
from fastapi import APIRouter, Request

router = APIRouter(prefix='/auth')

@router.post('/login')
def authenticate_user(data: LoginRequest, request: Request):
    ip_address = request.headers.get('x-forwarded-for') or request.client.host
    user_agent = request.headers.get('user-agent')
    print(data.__dict__) # TODO Call mmdpawn API