from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from app.api.articles import get_all_articles
from app.schemas.articles import ArticleResponse
from app.templates import templates


router = APIRouter(tags=["Articles"])


@router.get("/", response_class=HTMLResponse, name="articles:list")
async def get_articles_list(
    request: Request,
    articles: Annotated[list[ArticleResponse], Depends(get_all_articles)],
):
    return templates.TemplateResponse(
        request=request,
        name="articles.html",
        context={"articles": articles},
    )
