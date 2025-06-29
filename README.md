# FinSentiment-AI-Powered-Financial-News-Sentiment-Dashboard
A modern, interactive web dashboard for financial news analysis, powered by state-of-the-art AI, NLP, and real-time data visualization.

🚀 Features
1. User Authentication
Secure user registration and login using Flask-Login.

Passwords are hashed for safety.

Each user gets a personalized dashboard experience.

2. Live Financial News Aggregation
Fetches the latest business and financial news headlines using APIs.

News is deduplicated and enriched for better insights.

3. AI-Powered Sentiment Analysis
Each news headline is analyzed using NLTK’s VADER sentiment analyzer.

Headlines are labeled as Positive, Negative, or Neutral.

Sentiment confidence scores are displayed as animated progress bars.

4. AI-Generated News Summaries
Uses HuggingFace’s BART transformer to generate concise, readable summaries of the latest news and sentiment.

Summaries are displayed at the top of the dashboard for quick insights.

5. AI-Generated Trend & Risk Insights
Extracts and summarizes key risks, bullish/bearish drivers, and noteworthy events from the news flow using an LLM.

Presents these insights as bullet points for fast decision-making.

6. Interactive Stock Price Charts
Users can enter any stock ticker (e.g., AAPL, TSLA, GOOGL).

Interactive Plotly charts display 5-year historical price data.

Chart titles and axes update dynamically with the selected ticker.

7. Key Fundamentals Display
Shows important company data: market cap, sector, industry, P/E ratios, open/high/low/prev close.

Data is fetched live using yfinance.

8. Sector/Peer Sentiment Comparison
Automatically detects the sector of the selected stock.

Calculates and displays the average sentiment for the sector.

Compares the selected stock’s sentiment to its sector average with color-coded feedback.

9. Responsive, Animated UI
Built with Bootstrap 5 and Animate.css for a modern, mobile-friendly look.

All charts and tables feature smooth transitions and animations.

10. Advanced Filtering
Filter news by sentiment (Positive/Negative/Neutral), keyword, or ticker.

Instantly updates the dashboard based on user selection.

11. Enriched News Table
Each news item displays extracted named entities (companies, people, etc.) and keywords.

Sentiment confidence for each headline is visualized.

12. Error Handling & User Feedback
Graceful handling of missing data (e.g., invalid ticker, no news).

Informative flash messages for user actions and errors.

📸 Screenshots
![image](https://github.com/user-attachments/assets/5ac41e6b-ac36-4707-9f28-da4cac66019b)


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
git clone https://github.com/yourusername/FinSentiment.git
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
