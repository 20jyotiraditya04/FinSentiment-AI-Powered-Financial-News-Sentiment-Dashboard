from transformers import BertTokenizer, BertForSequenceClassification
import torch
import numpy as np

# Load FinBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')
model = BertForSequenceClassification.from_pretrained('ProsusAI/finbert')

def analyze_sentiment_finbert(news_list):
    """
    Analyze sentiment using FinBERT (financial-optimized BERT model)
    Returns updated list with FinBERT sentiment scores and labels
    """
    for item in news_list:
        text = item['headline']
        
        # Tokenize and process text
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        
        # Get model predictions
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Convert to probabilities
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1).numpy()[0]
        
        # FinBERT labels: [negative, neutral, positive]
        item['neg'] = probs[0]  # Negative probability
        item['neu'] = probs[1]  # Neutral probability
        item['pos'] = probs[2]  # Positive probability
        item['compound'] = probs[2] - probs[0]  # Sentiment score (-1 to 1)
        
        # Assign sentiment label
        label_idx = np.argmax(probs)
        item['sentiment_label'] = ['Negative', 'Neutral', 'Positive'][label_idx]
        
        # For Bootstrap coloring
        if item['sentiment_label'] == 'Positive':
            item['row_class'] = 'table-success'
        elif item['sentiment_label'] == 'Negative':
            item['row_class'] = 'table-danger'
        else:
            item['row_class'] = 'table-secondary'
    
    return news_list

# Already uses FinBERT for sentiment analysis.
