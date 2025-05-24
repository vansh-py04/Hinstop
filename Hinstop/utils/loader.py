def load_stopwords(path="Hinstop/data/stopwords-hi.txt"):
    with open(path,'r',encoding="utf-8") as f:
        words = {sen.strip() for sen in f if sen.strip()}
    
    return words


