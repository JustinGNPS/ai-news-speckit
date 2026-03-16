from typing import List

from fastapi import APIRouter, Body, Query

from app.models.schemas import SentimentResult
from app.services.sentiment_service import analyze_single, analyze_texts


router = APIRouter()


@router.get("/", response_model=SentimentResult, summary="Analyze sentiment for single text (query param)")
def analyze_one_get(text: str = Query(..., description="Text to analyze")):
    return analyze_single(text)


@router.post("/", response_model=List[SentimentResult], summary="Analyze sentiment for texts (batch)")
def analyze_many(texts: List[str] = Body(..., embed=True, description="List of texts to analyze")):
    return analyze_texts(texts)


@router.post("/single", response_model=SentimentResult, summary="Analyze sentiment for single text (body)")
def analyze_one(text: str = Body(..., embed=True, description="Text to analyze")):
    return analyze_single(text)
