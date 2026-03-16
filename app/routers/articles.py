from typing import List

from fastapi import APIRouter

from app.models.schemas import Article
from app.services.news_service import fetch_latest_articles


router = APIRouter()


@router.get("/", response_model=List[Article], summary="Get latest news articles")
def get_articles():
    return fetch_latest_articles()
