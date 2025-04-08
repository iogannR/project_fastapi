from fastapi import APIRouter

from app.api.articles import router as articles_router


router = APIRouter(prefix="/api")

router.include_router(articles_router, prefix="/articles")