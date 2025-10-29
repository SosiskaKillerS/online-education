from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.api.deps import DBSession
from app.models.course import Course
from app.schemas.course import CourseRead

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/", response_model=list[CourseRead], summary="Get all courses")
async def list_courses(db:DBSession):
    result = await db.execute(select(Course))
    courses = result.scalars().all()
    return courses

@router.get("/{course_id}", response_model=CourseRead, summary="Get course by id")
async def get_course(course_id:int, db:DBSession):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalars().first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course