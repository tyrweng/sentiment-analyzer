import numpy as np
import sklearn
from train import train_model

def evaluate_model(mode):
    model, vectorizer, train, dev, test = train_model()
    train_vectors, train_text, train_labels = train
    dev_vectors, dev_text, dev_labels = dev
    test_vectors, test_text, test_labels = test 

    if mode == "dev":
        vectors = dev_vectors
        labels = dev_labels
        text = dev_text
    elif mode == "test":
        vectors = test_vectors
        labels = test_labels
        text = test_text
    else:
        raise ValueError("Invalid mode. Choose 'dev' or 'test'.")

    # Accuracy: Out of all reviews, how many were correctly classified as
    # positive or negative  
    # Precision: Out of all reviews classified as positive,
    # how many were actually positive
    # Recall: Out of all actual positive reviews, how many were correctly
    # classified as positive
    # F1-Score: Is the model balanced between precision and recall? The
    # harmonic mean of precision and recall
    classification_report = sklearn.metrics.classification_report(
        labels,
        model.predict(vectors)
    )

    print("Classification Report:\n", classification_report)
    
    # Displays where the model is making mistakes among TP, TN, FP, FN
    confusion_matrix = sklearn.metrics.confusion_matrix(
        labels,
        model.predict(vectors)
    )
    print("Confusion Matrix:\n", confusion_matrix)

    # Extract misclassified reviews
    preds = model.predict(vectors)
    probs = model.predict_proba(vectors)

    # Loop through reviews and filter out correctly classified ones, leaving only misclassified reviews
    misclassified = [(text[i], labels[i], preds[i], probs[i][0], probs[i][1])
                        for i in range(len(preds)) if preds[i] != labels[i]]
    
    # print("Misclassified Reviews:\n", misclassified)
    print("First 10 Misclassified Reviews:")
    for text, label, pred, prob_neg, prob_pos in misclassified[:10]:
        print(f"Text: {text}")
        print(f"Actual: {label}, Predicted: {pred}, Confidences: [{prob_neg}, {prob_pos}]")
        print()