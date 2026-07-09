import joblib
from fastapi import FastAPI, Request
from ml.src.predict_sentiment import predict_sentiment
from models import SentimentRequest, SentimentResponse

def startup():
    model = joblib.load("../models/model.joblib")
    vectorizer = joblib.load("../models/vectorizer.joblib")
    app.state.model = model
    app.state.vectorizer = vectorizer

def shutdown():
    pass
    
app = FastAPI()

app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

@app.post("/predict")
async def predict_route(request: SentimentRequest):
    # call inference pipeline
    prediction, confidence_scores = predict_sentiment(
        request.text,
        app.state.model,
        app.state.vectorizer
    )
    
    return SentimentResponse(
        sentiment=prediction,
        confidence_scores=confidence_scores.tolist()
    )