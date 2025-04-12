import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.categories import CategoryDAO
from app.database import db_connection
from app.schemas.categories import (
    CategoryResponse, 
    CreateCategorySchema,
    PartialUpdateCategorySchema, 
    UpdateCategorySchema,
)


router = APIRouter(tags=["Категории"])


@router.get("/", response_model=list[CategoryResponse])
async def get_all_categories(
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = CategoryDAO(session)
    return await dao.get_all_records()


@router.get("/{id_}")
async def get_category_by_id(
    id_: uuid.UUID,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
) -> CategoryResponse | None:
    dao = CategoryDAO(session)
    return await dao.get_record_by_id(id_)


@router.post("/", response_model=CategoryResponse)
async def create_category(
    create_category_schema: CreateCategorySchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = CategoryDAO(session)
    return await dao.create_record(create_category_schema)


@router.put("/{id_}", response_model=CategoryResponse)
async def update_category_by_id(
    id_: uuid.UUID,
    update_category_schema: UpdateCategorySchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = CategoryDAO(session)
    return await dao.update_record_by_id(id_, update_category_schema)


@router.patch("/{id_}", response_model=CategoryResponse)
async def partial_update_category_by_id(
    id_: uuid.UUID,
    partial_update_category_schema: PartialUpdateCategorySchema,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
):
    dao = CategoryDAO(session)
    return await dao.update_record_by_id(
        id_,
        partial_update_category_schema,
        partial=True,
    )
    
    
@router.delete("{id_}")
async def delete_category_by_id(
    id_: uuid.UUID,
    session: Annotated[
        AsyncSession, Depends(db_connection.session_dependency),
    ],
) -> dict:
    dao = CategoryDAO(session)
    await dao.delete_record_by_id(id_)
    return {
        "message": "deleted successfully",
    }
