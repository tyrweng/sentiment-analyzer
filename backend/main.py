import joblib
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ml.src.predict_sentiment import predict_sentiment
from models import SentimentRequest, SentimentResponse

def startup():
    model = joblib.load("./ml/models/model.joblib")
    vectorizer = joblib.load("./ml/models/vectorizer.joblib")
    app.state.model = model
    app.state.vectorizer = vectorizer

def shutdown():
    pass
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    startup()
@app.on_event("shutdown")
async def shutdown_event():
    shutdown()

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