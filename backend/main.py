import joblib
from fastapi import FastAPI, Request
from ml.src.predict_sentiment import predict_sentiment

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
async def run_inference(request: Request):
    # get request and extract text
    body = (await request.json())
    input_text = body["text"]

    # call inference pipeline
    prediction, confidence_scores = predict_sentiment(
        input_text,
        app.state.model,
        app.state.vectorizer
    )

    # predict proba returns a numpy array, convert to list for JSON serialization
    return {"prediction": prediction, "confidence_scores": confidence_scores.tolist()}