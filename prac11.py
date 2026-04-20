from gensim.models import Word2Vec

# Simple demonstration of tokenization
text = "playing football"

# Word-level tokenization
word_tokens = text.split()

# Subword tokenization (simple demo representation)
subword_tokens = ["play", "ing", "football"]

print("Tokenization Comparison")
print("Word tokens:", word_tokens)
print("Subword tokens:", subword_tokens)
print("-" * 30)

# Minimal corpus for Word2Vec training demonstration
corpus = [
    ["i", "love", "nlp"], 
    ["machine", "learning", "is", "useful"], 
    ["i", "enjoy", "natural", "language", "processing"]
]

print("Training Word2Vec model on dummy corpus...")
w2v_model = Word2Vec(sentences=corpus, vector_size=10, window=3, min_count=1, workers=1)

print("\nSemantic Similarity using our tiny Word2Vec model:")
print("Similarity (love, enjoy):", w2v_model.wv.similarity("love", "enjoy"))
print("Similarity (nlp, learning):", w2v_model.wv.similarity("nlp", "learning"))
