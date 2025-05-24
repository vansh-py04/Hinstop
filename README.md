# Hinstop — Hindi Text Preprocessor & Sentiment Analyzer
Hinstop is a Python module for Hindi text preprocessing that combines stopword removal with lightweight sentiment scoring. Designed for developers and researchers working on Indic NLP, Hinstop offers an extensible interface similar to nltk or indicNLP, with additional support for custom stopword and sentiment lexicons.

✨ Features
🧹 Stopword Removal — Remove common Hindi stopwords using a curated list.

✍️ Custom Stopword Lists — Load your own stopwords for domain-specific filtering.

😄 Sentiment Scoring — Match positive and negative words to compute simple sentiment scores.

📊 Stopword Coverage — Estimate how noisy a text is based on stopword density.

🧠 Modular Design — Use StopwordRemover or Analyzer classes independently.

🔁 Batch Support — Analyze multiple sentences or documents easily.

🔌 Plug-and-Play — Integrates well into any preprocessing pipeline.

---
# 📦 Installation

## Clone the repository:
    git clone https://github.com/vansh-py04/hinstop.git
    cd hinstop
   
---
# 📂 Project Structure

Hinstop/
├── processor.py          # Main module (StopwordRemover & Analyzer)

├── utils/

│   └── loader.py         # Loads stopword/lexicon files

├── data/

│   ├── stopwords.txt     # Default stopword list

│   ├── positive.txt      # Optional sentiment words

│   └── negative.txt

└── test/

    └── demo.ipynb        # Interactive demo notebook
