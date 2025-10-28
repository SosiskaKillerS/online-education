from pydantic import BaseModel

class CategoryBase(BaseModel):
    name:str

class CategoryRequest(BaseModel):
    id: int
    name: str

class CategoryResponse(CategoryBase):
    pass

