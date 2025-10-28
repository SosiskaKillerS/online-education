from sqlalchemy import Column, TEXT, String
from sqlalchemy.orm import relationship
from app.core.db import Base
from app.models.user_course import user_course

class User(Base):
    __tablename__ = "user"
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(100), nullable=False)
    password = Column(TEXT, nullable = False)
    courses = relationship(
        "Course",
        secondary=user_course,
        back_populates="users"
    )


