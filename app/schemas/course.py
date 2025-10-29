from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

class CourseBase(BaseModel):
    title:str
    description:str
    study_time: int
    cost: Decimal
    format: str
    education_type: str
    issued_document: str
    category_id: int

class CourseRead(CourseBase):
    model_config = ConfigDict(from_attributes=True)