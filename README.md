FinSentiment: AI-Powered Financial News Sentiment Dashboard
A modern, interactive web dashboard for financial news analysis, powered by state-of-the-art AI, NLP, and real-time data visualization.

🚀 Features
User Authentication

Secure registration and login (Flask-Login)

Passwords are hashed for safety

Personalized dashboard experience

Live Financial News Aggregation

Fetches the latest business and financial news headlines using APIs

News is deduplicated and enriched for better insights

AI-Powered Sentiment Analysis

Each headline analyzed with NLTK’s VADER

Labeled as Positive, Negative, or Neutral

Sentiment confidence scores shown as animated progress bars

AI-Generated News Summaries

Uses HuggingFace’s BART transformer for concise summaries

Summaries shown at the top of the dashboard

AI-Generated Trend & Risk Insights

Extracts and summarizes key risks, drivers, and events using LLMs

Insights presented as bullet points for fast decision-making

Interactive Stock Price Charts

Enter any stock ticker (e.g., AAPL, TSLA, GOOGL)

Interactive Plotly charts display 5-year historical price data

Chart titles and axes update dynamically

Key Fundamentals Display

Shows company data: market cap, sector, industry, P/E ratios, open/high/low/prev close

Data fetched live using yfinance

Sector/Peer Sentiment Comparison

Detects sector of the selected stock

Calculates and displays sector average sentiment

Compares stock’s sentiment to sector average with color-coded feedback

Responsive, Animated UI

Built with Bootstrap 5 and Animate.css

Mobile-friendly and visually appealing

Advanced Filtering

Filter news by sentiment, keyword, or ticker

Dashboard updates instantly

Enriched News Table

Displays extracted entities and keywords for each news item

Visualizes sentiment confidence

Error Handling & User Feedback

Handles missing data gracefully (e.g., invalid ticker, no news)

Informative flash messages for actions and errors

📸 Screenshots
![image](https://github.com/user-attachments/assets/a17b4427-099d-49a6-86c0-63dbed5fd4a3)
![image](https://github.com/user-attachments/assets/0721cd9e-9d40-4234-9244-b3014c3487e6)
![image](https://github.com/user-attachments/assets/d37a6ed8-e9ae-4a04-a725-a27f50b01ee1)


🛠️ Tech Stack
Backend: Flask, Flask-Login, Flask-Migrate, SQLAlchemy

Frontend: Bootstrap 5, Animate.css, Plotly.js

AI/NLP: NLTK VADER, HuggingFace Transformers (BART)

Data: yfinance, NewsData.io (or similar)

Database: SQLite (default)

🏗️ Project Structure
text
FinSentiment/
├── app.py
├── routes.py
├── models.py
├── forms.py
├── news_fetcher.py
├── sentiment_analyzer.py
├── news_enrichment.py
├── stock_data.py
├── ai_summarizer.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
├── static/
│   └── (custom CSS, images, etc.)
├── instance/
│   └── app.db
├── requirements.txt
└── README.md
⚡ Getting Started
Clone the repository

bash
git clone https://github.com/20jyotiraditya04/FinSentiment-AI-Powered-Financial-News-Sentiment-Dashboard.git
cd FinSentiment
Create and activate a virtual environment

bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Set environment variables

bash
$Env:FLASK_APP = "app.py"
$Env:FLASK_ENV = "development"
Initialize the database

bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the app

bash
flask run
Visit http://127.0.0.1:5000/ in your browser.

💡 Inspiration
Yahoo Finance

Bloomberg Terminal

FinViz

📈 Roadmap
 User authentication

 Live news and sentiment analysis

 Interactive price charts and fundamentals

 Sector/peer comparison

 AI-generated summaries and trend/risk insights

 User watchlists and alerts (coming soon!)

 Dark mode toggle (coming soon!)

 More advanced charting and news sources (coming soon!)

🤝 Contributing
Pull requests and suggestions are welcome!
Please open an issue to discuss what you’d like to change.

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgements
HuggingFace Transformers

NLTK

Plotly

Bootstrap

Animate.css

Yahoo Finance (UI inspiration)

Built with ❤️ by Jyotiraditya
