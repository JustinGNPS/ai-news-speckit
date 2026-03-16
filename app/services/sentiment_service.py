from typing import List, Optional

from transformers import pipeline

from app.models.schemas import SentimentResult


# Lazy-load pipeline to avoid heavy init on module import
_sentiment_analyzer = None


def _get_analyzer():
    global _sentiment_analyzer
    if _sentiment_analyzer is None:
        _sentiment_analyzer = pipeline("sentiment-analysis")
    return _sentiment_analyzer


def analyze_texts(texts: List[str]) -> List[SentimentResult]:
    analyzer = _get_analyzer()
    results = []
    for text in texts:
        model_result = analyzer(text)[0]
        results.append(
            SentimentResult(
                label=model_result["label"],
                score=float(model_result["score"]),
                text=text,
            )
        )
    return results


def analyze_single(text: str) -> SentimentResult:
    return analyze_texts([text])[0]
