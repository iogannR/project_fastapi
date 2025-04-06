from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship,
)

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.articles import Article


class Category(Base):
    __tablename__ = "categories"
    
    name: Mapped[str] = mapped_column(String(60), unique=True)
    description: Mapped[str | None]
    
    articles: Mapped[list["Article"]] = relationship(
        back_populates="category",
    )
    
    def __str__(self) -> str:
        return f"<Category(name={self.name})>"
    
    def __repr__(self) -> str:
        return str(self)
