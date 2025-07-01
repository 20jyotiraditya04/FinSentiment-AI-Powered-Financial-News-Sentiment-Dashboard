from app import app, db, login_manager
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from forms import RegistrationForm, LoginForm
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

# Import your enrichment and sentiment modules
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from news_enrichment import deduplicate, add_entities, extract_keywords
from collections import Counter

# Import the AI summarizer
from ai_summarizer import generate_summary

# Import stock data and plotting, including sector comparison
from stock_data import get_historical_data, get_fundamentals, get_sector, analyze_sector_sentiment
import plotly.graph_objs as go

# Add this import for the transformers pipeline
from transformers import pipeline

# Initialize the summarizer at module level for efficiency
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_trend_risk_insights(headlines):
    """
    Use an LLM to extract top risks, bullish/bearish drivers, and noteworthy events from headlines.
    Returns a summary as bullet points.
    """
    input_text = "\n".join(headlines)
    prompt = (
        "Extract the top risks, bullish and bearish drivers, and noteworthy events from the following financial news headlines. "
        "Summarize them as concise bullet points."
    )
    full_input = prompt + "\n" + input_text
    # Set max_length to 99 to avoid warnings
    summary = summarizer(full_input, max_length=99, min_length=50, do_sample=False)[0]['summary_text']
    return summary

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    ticker = request.args.get('ticker', 'AAPL').upper()
    news = fetch_news()
    news = deduplicate(news)
    news = add_entities(news)
    news = extract_keywords(news)
    news_with_sentiment = analyze_sentiment(news)

    sentiment_filter = request.args.get('sentiment')
    keyword_filter = request.args.get('keyword', '').lower()

    filtered_news = []
    for item in news_with_sentiment:
        if sentiment_filter and item['sentiment_label'] != sentiment_filter:
            continue
        if keyword_filter and keyword_filter not in item['headline'].lower():
            continue
        filtered_news.append(item)
    if not sentiment_filter and not keyword_filter:
        filtered_news = news_with_sentiment

    columns = [col for col in filtered_news[0].keys() if col != 'row_class'] if filtered_news else []
    sentiment_counts = Counter([item['sentiment_label'] for item in filtered_news])

    # Compute sentiment summary and average sentiment for summarization
    total = len(filtered_news)
    if total > 0:
        pos_count = sum(1 for item in filtered_news if item['sentiment_label'] == 'Positive')
        neg_count = sum(1 for item in filtered_news if item['sentiment_label'] == 'Negative')
        neu_count = sum(1 for item in filtered_news if item['sentiment_label'] == 'Neutral')

        if pos_count >= neg_count and pos_count >= neu_count:
            sentiment_summary = 'Positive'
        elif neg_count >= pos_count and neg_count >= neu_count:
            sentiment_summary = 'Negative'
        else:
            sentiment_summary = 'Neutral'

        avg_sentiment = sum(item.get('compound', 0) for item in filtered_news) / total

        # Extract headlines for summarization
        headlines = [item['headline'] for item in filtered_news]

        # Generate summary using AI summarizer
        summary_text = generate_summary(headlines, sentiment_summary, avg_sentiment)

        # Generate trend/risk insights using LLM
        trend_risk_insights = generate_trend_risk_insights(headlines)
    else:
        summary_text = "No news to summarize."
        trend_risk_insights = "No trend/risk insights available."

    # Get stock data
    hist = get_historical_data(ticker, period="5y")  # Fetch 5 years of historical data
    fundamentals = get_fundamentals(ticker)

    # Create Plotly chart and pass as JSON
    if hist.empty or "Close" not in hist.columns:
        flash(f"No historical data available for {ticker}.", 'warning')
        price_chart_json = None
    else:
        # Ensure index is datetime and sorted
        hist = hist.sort_index()
        hist = hist[hist['Close'].notnull()]
        x_dates = hist.index.strftime('%Y-%m-%d').tolist()
        y_close = hist['Close'].tolist()
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x_dates,
            y=y_close,
            mode='lines',
            name='Close Price',
            line=dict(color='#4f8cff', width=3)
        ))
        fig.update_layout(
            title=f'Historical Price Chart ({ticker}, 5 Years)',
            yaxis_title='Price',
            xaxis_title='Date',
            height=400,
            plot_bgcolor='#f8fafc',
            paper_bgcolor='#fff',
            font=dict(family='Inter, Arial, sans-serif', size=14),
            margin=dict(l=40, r=40, t=50, b=40),
            hovermode='x unified',
            xaxis=dict(showgrid=True, gridcolor='#e3e9f7'),
            yaxis=dict(showgrid=True, gridcolor='#e3e9f7')
        )
        price_chart_json = fig.to_json()

    # Sector/peer sentiment comparison
    sector = get_sector(ticker)
    sector_avg_sentiment = analyze_sector_sentiment(sector, news_with_sentiment)
    ticker_news = [item for item in news_with_sentiment if ticker in item.get('headline', '')]
    if ticker_news:
        ticker_avg_sentiment = sum(item.get('compound', 0) for item in ticker_news) / len(ticker_news)
    else:
        ticker_avg_sentiment = None

    return render_template(
        'dashboard.html',
        records=filtered_news,
        columns=columns,
        sentiment_counts=sentiment_counts,
        summary_text=summary_text,
        trend_risk_insights=trend_risk_insights,
        ticker=ticker,
        fundamentals=fundamentals,
        price_chart_json=price_chart_json,
        sector=sector,
        sector_avg_sentiment=sector_avg_sentiment,
        ticker_avg_sentiment=ticker_avg_sentiment,
        avg_sentiment=avg_sentiment if total > 0 else 0  # Pass avg_sentiment for conclusion
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(email=form.email.data, phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

