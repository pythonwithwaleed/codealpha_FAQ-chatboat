"""Chatbot engine.

1. Preprocess text with NLTK (lowercase, tokenize, remove stopwords, stem)
2. Convert FAQs to TF-IDF vectors
3. Match the user's question with the most similar FAQ using cosine similarity
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------------- stopwords
def _load_stopwords():
    """Use NLTK's stopword list; download it once if missing; fall back
    to scikit-learn's list when offline."""
    try:
        from nltk.corpus import stopwords
        words = set(stopwords.words("english"))
    except LookupError:
        try:
            nltk.download("stopwords", quiet=True)
            from nltk.corpus import stopwords
            words = set(stopwords.words("english"))
        except Exception:
            words = set(ENGLISH_STOP_WORDS)
    words -= {"not", "no"}  # negations can change the meaning of a question
    return words


STOP_WORDS = _load_stopwords()
_tokenizer = RegexpTokenizer(r"[a-z0-9]+")
_stemmer = PorterStemmer()


# ------------------------------------------------------------ preprocessing
def preprocess(text: str) -> str:
    """Lowercase -> tokenize -> remove stopwords -> stem -> rejoin."""
    tokens = _tokenizer.tokenize(text.lower())
    tokens = [t for t in tokens if t not in STOP_WORDS]
    tokens = [_stemmer.stem(t) for t in tokens]
    return " ".join(tokens)


# ------------------------------------------------------------------- engine
class FAQBot:
    FALLBACK = ("Sorry, I couldn't find a good answer to that. "
                "Try rewording your question, or email support@shopeasy.example.")

    def __init__(self, faqs, threshold: float = 0.1):
        self.threshold = threshold
        self.questions = [f[0] for f in faqs]
        self.answers = [f[1] for f in faqs]

        # Question counts double; answer and alternative phrasings add context.
        corpus = [preprocess(f"{q} {q} {a} {kw}") for q, a, kw in faqs]
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(corpus)

    def ask(self, user_input: str):
        """Return (answer, matched_question or None, similarity score)."""
        cleaned = preprocess(user_input)
        if not cleaned:
            return "I didn't catch a question there. Could you rephrase it?", None, 0.0

        query_vec = self.vectorizer.transform([cleaned])
        scores = cosine_similarity(query_vec, self.matrix).flatten()
        best = int(scores.argmax())
        score = float(scores[best])

        if score < self.threshold:
            return self.FALLBACK, None, score
        return self.answers[best], self.questions[best], score
