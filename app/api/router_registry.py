from fastapi import APIRouter

from app.api.routers.db_health import router as db_health_router

api_router = APIRouter()

api_router.include_router(db_health_router)
