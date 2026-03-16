from datetime import datetime
from typing import List

import feedparser

from app.models.schemas import Article


BBC_RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"


def fetch_latest_articles() -> List[Article]:
    feed = feedparser.parse(BBC_RSS_URL)
    articles: List[Article] = []

    for entry in feed.entries:
        published_at = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_at = datetime(*entry.published_parsed[:6])

        summary = getattr(entry, "summary", None)
        article = Article(
            title=entry.title,
            link=entry.link,
            summary=summary,
            published_at=published_at,
            source="BBC",
        )
        articles.append(article)

    return articles
