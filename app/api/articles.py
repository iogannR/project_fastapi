from typing import Annotated
import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.articles import ArticleDAO
from app.schemas.articles import ArticleResponse, CreateArticleSchema, PartialUpdateArticleSchema, UpdateArticleSchema
from app.database import db_connection


router = APIRouter(tags=["Статьи"])


@router.get("/", response_model=list[ArticleResponse])
async def get_all_articles(
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = ArticleDAO(session)
    return await dao.get_all_records()


@router.get("/{id_}", response_model=ArticleResponse)
async def get_article_by_id(
    id_: uuid.UUID, 
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = ArticleDAO(session)
    return await dao.get_record_by_id(id_)


@router.post("/", response_model=ArticleResponse)
async def create_article(
    create_schema: CreateArticleSchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = ArticleDAO(session)
    return await dao.create_record(create_schema)


@router.put("/{id_}", response_model=ArticleResponse)
async def update_article_by_id(
    id_: uuid.UUID,
    update_schema: UpdateArticleSchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = ArticleDAO(session)
    return await dao.update_record_by_id(id_, update_schema)


@router.patch("/{id_}", response_model=ArticleResponse)
async def partial_update_article_by_id(
    id_: uuid.UUID,
    update_schema: PartialUpdateArticleSchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = ArticleDAO(session)
    return await dao.update_record_by_id(
        id_, 
        update_schema, 
        partial=True,
    )
    

@router.delete("/{id_}")
async def delete_article_by_id(
    id_: uuid.UUID,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
) -> dict:
    dao = ArticleDAO(session)
    await dao.delete_record_by_id(id_)
    return {
        "message": "deleted successfully",
    }
