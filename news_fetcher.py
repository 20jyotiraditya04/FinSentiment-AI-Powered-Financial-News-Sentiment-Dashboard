import requests

API_KEY = 'pub_ac030f0847564fa59fe3c8e966ac7ce6'  # Replace with your real API key

def fetch_news():
    url = f'https://newsdata.io/api/1/news?apikey={API_KEY}&language=en&category=business'
    response = requests.get(url)
    try:
        data = response.json()
    except Exception:
        return []
    news_list = []
    if isinstance(data, dict) and 'results' in data:
        for article in data['results']:
            if isinstance(article, dict):
                news_list.append({
                    'headline': article.get('title', ''),
                    'source': article.get('source_id', 'NewsData.io')
                })
    return news_list
