from fastapi import APIRouter
from sqlalchemy import text
from app.api.deps import DBSession

router = APIRouter(
    prefix="/db_health",
    tags=["db health"]
)

@router.get("", summary="Response from service")
async def health_service():
    return {"status":"ok"}

@router.get("/db", summary="DB health")
async def health_db(db: DBSession):
    result = await db.execute(text("SELECT 1 AS ok"))
    row = result.mappings().first()
    db_ok = row is not None and row["ok"]==1

    return {
        "status": "ok" if db_ok else "fail",
        "db": db_ok,
    }
