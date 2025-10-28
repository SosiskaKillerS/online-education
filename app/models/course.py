from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Integer,
    Numeric,
    ForeignKey,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.user_course import user_course


class Course(Base):
    __tablename__ = "course"

    id = Column(BigInteger, primary_key=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    study_time = Column(Integer, nullable=True)
    cost = Column(Numeric(10, 2), nullable=True)
    format = Column(String(100), nullable=True)
    education_type = Column(String(100), nullable=True)
    issued_document = Column(String(255), nullable=True)

    category_id = Column(
        BigInteger,
        ForeignKey("category.id"),
        nullable=False,
    )

    created_at = Column(TIMESTAMP(timezone=False), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=False), nullable=True)

    category = relationship(
        "Category",
        back_populates="courses",
    )

    users = relationship(
        "User",
        secondary=user_course,
        back_populates="courses",
    )
