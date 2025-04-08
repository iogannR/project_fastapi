import uvicorn
from fastapi import FastAPI

from app.api import router as api_router



def create_app() -> FastAPI:
    app = FastAPI(
        title="Статьи по информацонной безопасности",
        description="Сайт со статьями по информационной безопасности.",
    )
    app.include_router(api_router, prefix="/api")
    
    return app


if __name__ == "__main__":
    uvicorn.run(
        "app.main:create_app",
        reload=True,
        factory=True,
    )