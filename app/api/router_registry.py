from fastapi import APIRouter

from app.api.routers.db_health import router as db_health_router
from app.api.routers.course import router as course_router

api_router = APIRouter()

api_router.include_router(db_health_router)
api_router.include_router(course_router)
