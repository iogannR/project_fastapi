import uuid

from pydantic import BaseModel, ConfigDict


class CreateArticleSchema(BaseModel):
    title: str
    description: str | None = None
    image_name: str | None = None
    content: str
    category_id: uuid.UUID
    

class UpdateArticleSchema(CreateArticleSchema):
    ...
    

class PartialUpdateArticleSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    image_name: str | None = None
    content: str | None = None
    category_id: uuid.UUID | None = None
    


class ArticleResponse(CreateArticleSchema):
    id: uuid.UUID
    
    model_config = ConfigDict(
        from_attributes=True,
    )