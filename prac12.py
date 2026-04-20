import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download necessary NLTK components dynamically if missing
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

raw_text = "Natural language processing is interesting and highly useful."

print("Original Text:", raw_text)

# 1. Text Cleaning
lowered = raw_text.lower()
cleaned = lowered.translate(str.maketrans("", "", string.punctuation))

# 2. Tokenization
tokens = cleaned.split()

# 3. Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# 4. Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print("\nProcessed Words:", stemmed_tokens)

# 5. Feature Extraction (BoW & TF-IDF)
corpus = [" ".join(stemmed_tokens)]

bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(corpus)
print("\nBoW Words:", bow_vectorizer.get_feature_names_out())
print("BoW Matrix:", bow_matrix.toarray())

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
print("\nTF-IDF Words:", tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Matrix:", tfidf_matrix.toarray())
