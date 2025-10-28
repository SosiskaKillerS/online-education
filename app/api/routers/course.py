from fastapi import APIRouter
from app.api.deps import DBSession

router = APIRouter(
    prefix="courses",
    tags=["courses"]
)

@router.get("")
async def get_courses(db:DBSession):
    pass
