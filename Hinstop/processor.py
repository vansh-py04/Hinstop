# processor.py
from .utils.loader import load_stopwords
from indicnlp.tokenize import indic_tokenize
from typing import List, Optional, Literal

class StopwordRemover:
    def __init__(
        self,
        method: Literal["default", "custom"] = "default",
        lang: str = "hi",
        custom_stopwords: Optional[List[str]] = None
    ):
        self.lang = lang
        if method == "default":
            self.stopwords = load_stopwords()
        elif method == "custom":
            if custom_stopwords is None:
                raise ValueError("custom_stopwords must be provided")
            self.stopwords = custom_stopwords
        else:
            raise ValueError("Invalid method")

    def remove(self, text: str) -> str:
        tokens = indic_tokenize.trivial_tokenize(text, self.lang)
        return " ".join([word for word in tokens if word not in self.stopwords])

    def coverage(self, text: str) -> float:
        tokens = indic_tokenize.trivial_tokenize(text, self.lang)
        return len([t for t in tokens if t in self.stopwords]) / len(tokens)


class Analyzer(StopwordRemover):
    def __init__(
        self,
        method: Literal["default", "custom"] = "default",
        lang: str = "hi",
        custom_stopwords: Optional[List[str]] = None,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None
    ):
        super().__init__(method=method, lang=lang, custom_stopwords=custom_stopwords)
        self.positive_words = positive_words or []
        self.negative_words = negative_words or []

    def positive_score(self, text: str) -> int:
        tokens = indic_tokenize.trivial_tokenize(text, self.lang)
        return sum(1 for token in tokens if token in self.positive_words)

    def negative_score(self, text: str) -> int:
        tokens = indic_tokenize.trivial_tokenize(text, self.lang)
        return sum(1 for token in tokens if token in self.negative_words)

    def sentiment_score(self, text: str) -> dict:
        pos = self.positive_score(text)
        neg = self.negative_score(text)
        total = pos + neg

        if total == 0:
            return {
                "Score": None,
                "Label": "neutral",
                "Positive Count": pos,
                "Negative Count": neg
            }

        score = pos / total
        label = "positive" if score > 0.5 else "negative" if score < 0.5 else "neutral"

        return {
            "Score": score,
            "Label": label,
            "Positive Count": pos,
            "Negative Count": neg
        }

    def analyze(self, text: str) -> dict:
        return {
            "cleaned": self.remove(text),
            "coverage": self.coverage(text),
            "sentiment": self.sentiment_score(text)
        }

