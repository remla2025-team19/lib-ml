import pickle

def save_vectorizer(vectorizer, path):
    with open(path, 'wb') as f:
        pickle.dump(vectorizer, f)

def load_vectorizer(path):
    with open(path, 'rb') as f:
        return pickle.load(f)