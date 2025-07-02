from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure the VADER lexicon is downloaded (run once)
nltk.download('vader_lexicon', quiet=True)

# NOTE: This file is not used if FinBERT is used for sentiment analysis in the backend.

def analyze_sentiment(news_list):
    """
    Adds sentiment scores and labels to each news dict in the list.
    Returns the updated list.
    """
    sia = SentimentIntensityAnalyzer()
    for item in news_list:
        sentiment = sia.polarity_scores(item.get('headline', ''))
        item.update(sentiment)
        # Add sentiment label
        if item['compound'] > 0.05:
            item['sentiment_label'] = 'Positive'
            item['row_class'] = 'table-success'
        elif item['compound'] < -0.05:
            item['sentiment_label'] = 'Negative'
            item['row_class'] = 'table-danger'
        else:
            item['sentiment_label'] = 'Neutral'
            item['row_class'] = 'table-secondary'
    return news_list
