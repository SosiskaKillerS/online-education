from sqlalchemy import Column, BigInteger, Table, ForeignKey
from app.core.db import Base

user_course = Table(
    "user_course",
    Base.metadata,
    Column("user_id", BigInteger, ForeignKey("user.id"), primary_key=True),
    Column("course_id", BigInteger, ForeignKey("course.id"), primary_key=True)
)
