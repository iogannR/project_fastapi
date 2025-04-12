from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.views.articles import router as articles_html_router
from app.templates import templates


router = APIRouter()

@router.get("/", response_class=HTMLResponse, name="home")
async def get_home_page(
    request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )

router.include_router(articles_html_router, prefix="/articles")