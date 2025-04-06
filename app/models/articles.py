import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.categories import Category


class Article(Base):
    title: Mapped[str] = mapped_column(String(85), unique=True)
    description: Mapped[str | None]
    image_name: Mapped[str | None]
    content: Mapped[str] = mapped_column(Text)
    
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("categories.id"),
    )
    category: Mapped["Category"] = relationship(
        back_populates="articles",
    )
