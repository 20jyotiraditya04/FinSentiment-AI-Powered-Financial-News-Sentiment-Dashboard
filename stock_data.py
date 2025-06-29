import yfinance as yf

# Map sectors to a few representative tickers (expand as needed)
sector_tickers = {
    'Technology': ['AAPL', 'MSFT', 'GOOGL', 'INTC', 'CSCO'],
    'Financial Services': ['JPM', 'BAC', 'WFC', 'C', 'GS'],
    'Healthcare': ['JNJ', 'PFE', 'MRK', 'ABBV', 'TMO']
}

def get_historical_data(ticker, period="5y"):
    """Fetch historical price data for a ticker."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def get_fundamentals(ticker):
    """Fetch key fundamentals for a ticker."""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        'longName': info.get('longName', ticker),
        'marketCap': info.get('marketCap', 'N/A'),
        'trailingPE': info.get('trailingPE', 'N/A'),
        'forwardPE': info.get('forwardPE', 'N/A'),
        'open': info.get('open', 'N/A'),
        'high': info.get('dayHigh', 'N/A'),
        'low': info.get('dayLow', 'N/A'),
        'previousClose': info.get('previousClose', 'N/A'),
        'sector': info.get('sector', 'N/A'),
        'industry': info.get('industry', 'N/A')
    }

def get_sector(ticker):
    """Get the sector for a given ticker."""
    stock = yf.Ticker(ticker)
    return stock.info.get('sector', 'Unknown')

def analyze_sector_sentiment(sector, news_with_sentiment):
    """
    Calculate the average sentiment (compound score) for all news
    related to tickers in the given sector.
    """
    tickers = sector_tickers.get(sector, [])
    sector_news = [
        item for item in news_with_sentiment
        if any(ticker in item.get('headline', '') for ticker in tickers)
    ]
    if not sector_news:
        return None
    avg_compound = sum(item.get('compound', 0) for item in sector_news) / len(sector_news)
    return avg_compound
