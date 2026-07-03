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
    misclassified = [(text, label, pred, probs[i][pred])
                        for i, (text, label, pred) in
                        enumerate(zip(text, labels, preds))
                        if label != pred]
    print("Misclassified Reviews:\n", misclassified)