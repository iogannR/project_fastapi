from fastapi import APIRouter

from app.api.articles import router as articles_router
from app.api.categories import router as categories_router


router = APIRouter(prefix="/api")

router.include_router(articles_router, prefix="/articles")
router.include_router(categories_router, prefix="/categories")
