from fastapi import APIRouter
from app.api.v1.inventory_router import router as inventory_router

v1_router = APIRouter(prefix='/api/v1')
v1_router.include_router(inventory_router)