import uuid

from pydantic import BaseModel, ConfigDict


class CreateCategorySchema(BaseModel):
    name: str
    description: str | None = None
    

class UpdateCategorySchema(CreateCategorySchema):
    ...
    
    
class PartialUpdateCategorySchema(BaseModel):
    name: str | None = None
    description: str | None = None


class CategoryResponse(CreateCategorySchema):
    id: uuid.UUID
    
    model_config = ConfigDict(
        from_attributes=True,
    )
