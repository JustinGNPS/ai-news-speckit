from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    title: str
    link: HttpUrl
    summary: Optional[str] = None
    published_at: Optional[datetime] = None
    source: Optional[str] = None


class SentimentResult(BaseModel):
    label: str
    score: float
    text: str
