from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.core.db import get_session

DBSession = Annotated[AsyncSession, Depends(get_session)]