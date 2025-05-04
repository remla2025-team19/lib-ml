import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class TextPreprocessor:
    def __init__(self):
        self.ps = PorterStemmer()
        self.all_stopwords = self._load_stopwords()
        
    def _load_stopwords(self):
        nltk.download('stopwords', quiet=True)
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        return all_stopwords
        
    def preprocess_text(self, text):
        if not isinstance(text, str):
            return ""
            
        review = re.sub('[^a-zA-Z]', ' ', text)
        review = review.lower()
        review = review.split()
        review = [self.ps.stem(word) for word in review if word not in set(self.all_stopwords)]
        return ' '.join(review)
        
    def preprocess_texts(self, texts):
        return [self.preprocess_text(text) for text in texts]
    

if __name__ == '__main__':
    pass