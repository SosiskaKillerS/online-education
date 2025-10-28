from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from app.core.db import Base
from sqlalchemy.orm import relationship
from app.models.user_course import user_course

class Course(Base):
    __tablename__ = "course"
    id = Column(BigInteger, primary_key = True)
    title = Column(String(255), nullable = False)
    description = Column(Text, nullable = True)
    category_id = Column(
        BigInteger,
        ForeignKey("category.id"),
        nullable = False
    )
    category = relationship(
        "Category",
        back_populates="courses"
    )

    users = relationship(
        "User",
        secondary=user_course,
        back_populates="courses"
    )


