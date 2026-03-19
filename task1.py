# Import required libraries
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Input data
text_data = [
    "NLP is amazing! Learning models and patterns.",
    "Learning NLP is fun and powerful.",
    "Deep learning improves NLP applications.",
    "Text data requires cleaning and preprocessing.",
    "Natural Language Processing is widely used in AI.",
    "AI models learn from large amounts of text data.",
    "Preprocessing text is an important step in NLP.",
    "Machine learning and deep learning are related fields."
]

stemmer = PorterStemmer()

# Preprocessing function
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stemming
    tokens = [stemmer.stem(word) for word in tokens]
    
    return " ".join(tokens)

# now i am going to apply preprocessing for getting cleaned text
cleaned_text = [preprocess_text(text) for text in text_data]

# Print cleaned text
print("************Cleaned Text************:")
for i, text in enumerate(cleaned_text):
    print(f"{i+1}. {text}")

# ************------------------ Bag of Words ------------------***********
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(cleaned_text)

print("\n▶️  BoW Matrix Shape:", bow_matrix.shape)

# ************------------------ TF-IDF ------------------************
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_text)

print("▶️  TF-IDF Matrix Shape:", tfidf_matrix.shape)