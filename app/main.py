from fastapi import FastAPI

from app.routers import articles, sentiment


def create_app() -> FastAPI:
    app = FastAPI(title="AI News Sentiment API", version="0.1.0")

    app.include_router(articles.router, prefix="/articles", tags=["articles"])
    app.include_router(sentiment.router, prefix="/sentiment", tags=["sentiment"])

    @app.get("/", summary="Health check")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
