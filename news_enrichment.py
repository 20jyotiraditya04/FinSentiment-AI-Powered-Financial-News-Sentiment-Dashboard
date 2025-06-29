import spacy

nlp = spacy.load("en_core_web_sm")

def deduplicate(news_list):
    seen = set()
    unique_news = []
    for item in news_list:
        headline = item['headline']
        if headline not in seen:
            unique_news.append(item)
            seen.add(headline)
    return unique_news

def add_entities(news_list):
    for item in news_list:
        doc = nlp(item['headline'])
        item['entities'] = [(ent.text, ent.label_) for ent in doc.ents]
    return news_list

def extract_keywords(news_list):
    for item in news_list:
        doc = nlp(item['headline'])
        item['keywords'] = [chunk.text for chunk in doc.noun_chunks]
    return news_list
