import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class TextPreprocessor:
    def __init__(self):
        self.ps = PorterStemmer()
        self.all_stopwords = self._load_stopwords()
        
    def _load_stopwords(self):
        """Load English stopwords, excluding 'not'"""
        nltk.download('stopwords', quiet=True)
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        return all_stopwords
        
    def preprocess_text(self, text):
        """Clean and preprocess a single review text"""
        review = re.sub('[^a-zA-Z]', ' ', str(text))
        review = review.lower()
        review = review.split()
        review = [self.ps.stem(word) for word in review if word not in set(self.all_stopwords)]
        return ' '.join(review)
        
    def preprocess_texts(self, texts):
        """Process multiple texts"""
        return [self.preprocess_text(text) for text in texts]
        
    def get_corpus(self, dataset, text_column='Review'):
        """Get corpus from dataset - for backward compatibility"""
        corpus = []
        for i in range(len(dataset)):
            review = self.preprocess_text(dataset[text_column][i])
            corpus.append(review)
        return corpus