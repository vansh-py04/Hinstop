# Hinstop — Hindi Text Preprocessor & Sentiment Analyzer
Hinstop is a Python module for Hindi text preprocessing that combines stopword removal with lightweight sentiment scoring. Designed for developers and researchers working on Indic NLP, Hinstop offers an extensible interface similar to nltk or indicNLP, with additional support for custom stopword and sentiment lexicons.

✨ Features
  1. Stopword Removal — Remove common Hindi stopwords using a curated list.

  2. Custom Stopword Lists — Load your own stopwords for domain-specific filtering.

  3. Sentiment Scoring — Match positive and negative words to compute simple sentiment scores.

  4. Stopword Coverage — Estimate how noisy a text is based on stopword density.

  5. Modular Design — Use StopwordRemover or Analyzer classes independently.

  6. Plug-and-Play — Integrates well into any preprocessing pipeline.

---
# 📦 Installation

## Clone the repository:
    git clone https://github.com/vansh-py04/hinstop.git
    cd hinstop
---
## Example : Analyzing Hindi Text
````
from Hinstop.processor import Analyzer

text = "यह एक बहुत अच्छा दिन है लेकिन थोड़ी परेशानी भी थी।"
positive = ["अच्छा", "शानदार"]
negative = ["परेशानी", "खराब"]

analyzer = Analyzer(method="default", positive_words=positive, negative_words=negative)
result = analyzer.analyze(text)

print(result)
````

## Output

````
{
  'cleaned': 'अच्छा दिन थोड़ी परेशानी थी।',
  'coverage': 0.5,
  'sentiment': {
    'Score': 0.5,
    'Label': 'neutral',
    'Positive Count': 1,
    'Negative Count': 1
  }
}
````


---
# Functionality Overview

| Method                       | Description                                                                 |
| ---------------------------- | --------------------------------------------------------------------------- |
| `StopwordRemover.__init__()` | Initializes with default or custom stopword list and sets language          |
| `StopwordRemover.remove()`   | Removes all stopwords from the input Hindi text                             |
| `StopwordRemover.coverage()` | Calculates the ratio of stopwords in the input text (i.e., noise level)     |
| `Analyzer.__init__()`        | Inherits from `StopwordRemover`; adds support for sentiment word lists      |
| `Analyzer.positive_score()`  | Returns the number of matched positive words in the input text              |
| `Analyzer.negative_score()`  | Returns the number of matched negative words in the input text              |
| `Analyzer.sentiment_score()` | Computes sentiment polarity (`positive`, `negative`, `neutral`) and score   |
| `Analyzer.analyze()`         | Performs full analysis: cleaned text, stopword coverage, and sentiment info |


