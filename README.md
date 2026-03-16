# AI News Sentiment API

## 專案簡介
基於 FastAPI 的新聞收集與情緒分析最小實作，新聞來源使用 BBC Top Stories RSS，情緒分析採用 HuggingFace transformers `sentiment-analysis` pipeline。

## 專案結構
```
app/
  __init__.py
  main.py
  models/
    __init__.py
    schemas.py         # Pydantic models: Article, SentimentResult
  services/
    __init__.py
    news_service.py    # BBC RSS 抓取
    sentiment_service.py # transformers pipeline
  routers/
    __init__.py
    articles.py        # GET /articles
    sentiment.py       # POST /sentiment, POST /sentiment/single
requirements.txt
```

## 安裝與執行
```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API 說明
- `GET /`：健康檢查
- `GET /articles`：取得 BBC RSS 最新文章
- `POST /sentiment`：分析多筆文字，body: `{ "texts": ["...", "..."] }`
- `POST /sentiment/single`：分析單筆文字，body: `{ "text": "..." }`

## 注意
- transformers 會首次下載模型，需網路連線。
- Windows ARM64 以 `torch==2.2.1`，其他平台採 `torch>=2.2.0`（可依實際環境調整）。
