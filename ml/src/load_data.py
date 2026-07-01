from datasets import load_dataset

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
    # Each row looks like: {'text': 'I loved this movie!', 'label': 1} 
    # 0 = negative, 1 = positive
    dataset = load_dataset("imdb")
    return dataset["train"], dataset["test"]