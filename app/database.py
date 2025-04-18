from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession
)

from app.config import settings


class DatabaseConnection:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )
        
    async def dispose(self) -> None:
        return await self.engine.dispose()
    
    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            
            
db_connection = DatabaseConnection(
    url=str(settings.db.url),
    echo=settings.db.echo,
)
