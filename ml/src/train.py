from load_data import load_imdb_dataset
from preprocess import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
    # load the IMDB dataset
    train_data, test_data = load_imdb_dataset()

    # apply the clean_data function to the text data in both train and test datasets
    train_data = train_data.map(lambda row: {"text": clean_text(row["text"])})
    test_data = test_data.map(lambda row: {"text": clean_text(row["text"])})

    # extract the text and labels from the datasets
    train_text = train_data["text"]
    train_labels = train_data["label"]

    test_text = test_data["text"]
    test_labels = test_data["label"]

    # vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer(
        min_df=3,
        max_df=0.95,
        ngram_range=(1, 2)
    )
    train_vectors = vectorizer.fit_transform(train_text)
    test_vectors = vectorizer.transform(test_text)

    # Training
    reg = LogisticRegression(
        max_iter=1000,
        solver='liblinear',
        random_state=42
    ).fit(train_vectors, train_labels)

    return reg, vectorizer, test_vectors, test_text, test_labels