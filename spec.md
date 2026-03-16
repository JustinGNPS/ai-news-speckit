# AI News Sentiment Analysis Specification

## Goal
Build a simple AI system that collects news and performs sentiment analysis.

## Features

### News Collection
Fetch news from RSS feeds or APIs.

### Sentiment Analysis
Analyze text sentiment and classify as:
- Positive
- Neutral
- Negative

### Backend API
Provide REST endpoints.

GET /articles
GET /sentiment

### Dashboard
Display news and sentiment trends.

## Technology

Backend: FastAPI  
NLP: HuggingFace Transformers  
Frontend: React