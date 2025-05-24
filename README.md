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
    ```from Hinstop.processor import Analyzer

    text = "यह एक बहुत अच्छा दिन है लेकिन थोड़ी परेशानी भी थी।"
    positive = ["अच्छा", "शानदार"]
    negative = ["परेशानी", "खराब"]

    analyzer = Analyzer(method="default", positive_words=positive, negative_words=negative)
    result = analyzer.analyze(text)

    print(result)```

---
# 📂 Project Structure

Hinstop/
├── processor.py              # Main module with StopwordRemover and Analyzer classes
│
├── utils/                    # Utility functions
│   ├── __init__.py
│   └── loader.py             # Functions to load stopword, positive, and negative word lists
│
├── data/                     # Default word lists
│   ├── stopwords.txt         # Default Hindi stopwords
│   ├── positive.txt          # Optional list of positive sentiment words
│   └── negative.txt          # Optional list of negative sentiment words
│
├── test/                     # Demos and test scripts
│   ├── __init__.py
│   ├── demo.py               # Example script to test the module
│   └── demo.ipynb            # Jupyter notebook demo
│
├── __init__.py               # Package initializer
└── README.md                 # Project documentation

