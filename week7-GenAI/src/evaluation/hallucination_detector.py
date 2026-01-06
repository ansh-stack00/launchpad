from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def detect_hallucination(answer: str, context: str, threshold: float = 0.25):
  
    if not context.strip():
        return True, 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    vectors = vectorizer.fit_transform([answer, context])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    is_hallucinated = score < threshold

    return is_hallucinated, round(score, 3)
