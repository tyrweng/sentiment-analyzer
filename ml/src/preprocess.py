def clean_data(text):
    # lowercase text, expand contractions, remove punctuation, normalize whitespace,
    # strip leading/trailing whitespace
    # lowercase text
    text = text.lower()
    # expand contractions
    contractions = {
        "can't": "cannot",
        "won't": "will not",
        "ain't": "is not",
        "y'all": "you all",
        "n't": " not",
        "'re": " are",
        "'s": " is",
        "'d": " would",
        "'ll": " will",
        "'t": " not",
        "'ve": " have",
        "'m": " am"
    }
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    # remove punctuation and normalize whitespace
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    # strip leading/trailing whitespace
    text = ' '.join(text.split())
    return text