from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.models.articles import Article


class ArticleDAO(BaseDAO[Article]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Article)
