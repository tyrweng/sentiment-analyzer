from datasets import load_dataset
from preprocess import clean_text
from sklearn.model_selection import train_test_split

def load_imdb_dataset():
    # Format is a dictionary with 'train' and 'test' keys
    #DatasetDict({
    #     train: Dataset({
    #         features: ['text', 'label'],
    #         num_rows: 25000
    #     })
    #     test: Dataset({
    #         features: ['text', 'label'],
    #         num_rows: 25000
    #     })
    #     unsupervised: Dataset({
    #         features: ['text', 'label'],
    #         num_rows: 50000
    #     })
    # })
    # Each row looks like: {'text': 'I loved this movie!', 'l               abel': 1} 
    # 0 = negative, 1 = positive
    dataset = load_dataset("stanfordnlp/imdb")
    train_data = dataset["train"]
    test_data = dataset["test"]

    # Split the training data into a new training set and a development set (80% train, 20% dev)
    split = train_data.train_test_split(test_size=0.2, seed=42)
    train_data = split["train"]
    dev_data = split["test"]

    # apply the clean_data function to the text data in both train and test datasets
    train_data = train_data.map(lambda row: {"text": clean_text(row["text"])})
    dev_data = dev_data.map(lambda row: {"text": clean_text(row["text"])})
    test_data = test_data.map(lambda row: {"text": clean_text(row["text"])})

    return train_data, dev_data, test_data