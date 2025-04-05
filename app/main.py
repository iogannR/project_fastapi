import uvicorn
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Статьи по информацонной безопасности",
        description="Сайт со статьями по информационной безопасности.",
    )
    
    return app


if __name__ == "__main__":
    uvicorn.run(
        "app.main:create_app",
        reload=True,
        factory=True,
    )