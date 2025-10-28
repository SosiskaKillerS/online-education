from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.core.db import Base

class Category(Base):
    __tablename__ = "category"
    id = Column(BigInteger, primary_key = True)
    name = Column(String(255), nullable=False)

    courses = relationship("Course", back_populates="category")
