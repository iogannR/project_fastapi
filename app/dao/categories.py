from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.models.categories import Category


class CategoryDAO(BaseDAO[Category]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Category)
