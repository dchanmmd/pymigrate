from fastapi import APIRouter
from app.api.v1.auth_router import router as auth_router
from app.api.v1.branch_router import router as branch_router
from app.api.v1.inventory_router import router as inventory_router
from app.api.v1.transfer_router import router as transfer_router

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(auth_router)
v1_router.include_router(branch_router)
v1_router.include_router(inventory_router)
v1_router.include_router(transfer_router)