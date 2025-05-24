# Hinstop — Hindi Text Preprocessor & Sentiment Analyzer
Hinstop is a Python module for Hindi text preprocessing that combines stopword removal with lightweight sentiment scoring. Designed for developers and researchers working on Indic NLP, Hinstop offers an extensible interface similar to nltk or indicNLP, with additional support for custom stopword and sentiment lexicons.

✨ Features
 Stopword Removal — Remove common Hindi stopwords using a curated list.

 Custom Stopword Lists — Load your own stopwords for domain-specific filtering.

 Sentiment Scoring — Match positive and negative words to compute simple sentiment scores.

 Stopword Coverage — Estimate how noisy a text is based on stopword density.

 Modular Design — Use StopwordRemover or Analyzer classes independently.

 Batch Support — Analyze multiple sentences or documents easily.

 Plug-and-Play — Integrates well into any preprocessing pipeline.

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

# StopwordRemover
Handles basic text preprocessing by removing Hindi stopwords.

Method	Description
__init__(...)	Initializes with either a default or user-defined stopword list.
remove(text)	Removes stopwords from the input Hindi text and returns the cleaned version.
coverage(text)	Calculates the percentage of stopwords in the input text (i.e., how “noisy” the text is).

# Analyzer (extends StopwordRemover)
Adds sentiment analysis functionality using positive and negative word matching.

Method	Description
__init__(...)	Initializes the analyzer with optional positive and negative word lists, and inherits stopword handling.
positive_score(text)	Counts how many positive words are present in the text.
negative_score(text)	Counts how many negative words are present in the text.
sentiment_score(text)	Calculates a sentiment score and label (positive, negative, or neutral) based on word counts.
analyze(text)	Returns a complete analysis of the text: cleaned version, stopword coverage, sentiment label, score, and word counts.

