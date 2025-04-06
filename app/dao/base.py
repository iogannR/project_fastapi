import uuid
from typing import TypeVar, Generic, Sequence

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import Base


T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):
    def __init__(self, session: AsyncSession, model: type[T]) -> None:
        self._session = session
        self._model = model
        
    async def get_record_by_id(self, id_: uuid.UUID) -> T:
        return await self._session.get(self._model, id_)
    
    async def get_all_records(self) -> Sequence[T]:
        stmt = select(self._model).order_by(self._model.id)
        result: Result = await self._session.execute(stmt)
        return result.scalars().all()
    
    async def create_record(self, create_schema: BaseModel) -> None:
        record = self._model(**create_schema)
        self._session.add(record)
        await self._session.commit()
        await self._session.refresh(record)
        return record
    
    async def update_record_by_id(
        self, 
        id_: uuid.UUID, 
        update_schema: BaseModel, 
        partial: bool = False,
    ) -> T:
        record = await self._session.get(self._model, id_)
        if record:
            for key, value in update_schema.model_dump(exclude_unset=partial):
                setattr(record, key, value)
                
        await self._session.commit()
        await self._session.refresh(record)
        return record
    
    async def delete_record_by_id(self, id_: uuid.UUID) -> None:
        record = await self._session.get(self._model, id_)
        await self._session.delete(record)
        await self._session.commit()
