from preprocess import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_sentiment(input_text, model, vectorizer):
    # preprocess text
    cleaned_text = clean_text(input_text)
    
    # vectorize text
    text_vector = vectorizer.transform([cleaned_text])
    
    # run model prediction
    prediction = model.predict(text_vector)[0]

    # extract confidence scores
    confidence_scores = model.predict_proba(text_vector)[0]
    negative_confidence = confidence_scores[0]
    positive_confidence = confidence_scores[1]

    thresholds = {
        "positive": 0.6,
        "negative": 0.6
    }
    
    # map prediction to sentiment label
    if positive_confidence >= thresholds["positive"]:
        prediction = "positive"
    elif negative_confidence >= thresholds["negative"]:
        prediction = "negative"
    else:
        prediction = "neutral"
    
    return prediction, confidence_scores