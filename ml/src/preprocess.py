def clean_data(data):
    # lowercase text, expand contractions, remove punctuation, normalize whitespace,
    # strip leading/trailing whitespace
    for row in data:
        # lowercase text
        row['text'] = row['text'].lower()
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
            row['text'] = row['text'].replace(contraction, expansion)
        # remove punctuation and normalize whitespace
        row['text'] = ''.join(char for char in row['text'] if char.isalnum() or char.isspace())
        # strip leading/trailing whitespace
        row['text'] = ' '.join(row['text'].split())
    return data