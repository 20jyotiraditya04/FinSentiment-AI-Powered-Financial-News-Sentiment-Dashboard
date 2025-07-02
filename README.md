---

# 💹 FinSentiment: AI-Powered Financial News Sentiment Dashboard

A modern, interactive web dashboard for financial news analysis, powered by state-of-the-art AI, NLP, and real-time data visualization.

---

## 🚀 Features

### 🔐 User Authentication

* Secure registration and login using **Flask-Login**
* Passwords are securely **hashed**
* Personalized dashboard for each user

### 📰 Live Financial News Aggregation

* Fetches the **latest business/financial headlines** using news APIs
* Intelligent **deduplication and enrichment** for better insights

### 🧠 AI-Powered Sentiment Analysis

* Headlines analyzed using **NLTK’s VADER**
* Labels: **Positive**, **Negative**, or **Neutral**
* Confidence scores shown via **animated progress bars**

### ✍️ AI-Generated News Summaries

* Uses **HuggingFace’s BART transformer** for concise summaries
* Summaries displayed prominently on the dashboard

### 📊 AI-Generated Trend & Risk Insights

* Extracts key **risks, events, and drivers** from headlines using LLMs
* Presents insights as bullet points for quick decision-making

### 📈 Interactive Stock Price Charts

* Search any ticker (e.g., `AAPL`, `TSLA`, `GOOGL`)
* Displays **5-year historical price data** with Plotly
* Dynamic titles and axes based on the selected stock

### 🧾 Key Fundamentals Display

* Shows: **market cap**, **sector**, **P/E ratios**, **daily highs/lows**, etc.
* Live data pulled via **yfinance**

### 🔍 Sector/Peer Sentiment Comparison

* Auto-detects stock’s sector
* Compares stock sentiment with **sector average**
* Color-coded feedback based on comparison

### 🎨 Responsive, Animated UI

* Built using **Bootstrap 5** and **Animate.css**
* Mobile-friendly and clean visual design

### 🧠 Advanced Filtering

* Filter news by **sentiment**, **keyword**, or **ticker**
* Dashboard updates instantly

### 📚 Enriched News Table

* Shows extracted **entities and keywords**
* Includes **sentiment confidence visualizations**

### ⚠️ Error Handling & Feedback

* Handles missing or incorrect inputs gracefully
* Provides **informative flash messages** for errors/actions

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/b5239ed8-4f0c-4170-a978-dc4d24e10b19)
![image](https://github.com/user-attachments/assets/9bc63b1e-275c-4dfa-875d-7643aa01b901)
![image](https://github.com/user-attachments/assets/0e13f8d7-95e2-4811-bf1b-d837cd3e2ec8)

---

## 🛠️ Tech Stack

**Backend:** Flask, Flask-Login, Flask-Migrate, SQLAlchemy
**Frontend:** Bootstrap 5, Animate.css, Plotly.js
**AI/NLP:** NLTK (VADER), HuggingFace Transformers (BART)
**Data Sources:** yfinance, NewsData.io
**Database:** SQLite (default)

---

## 🗂️ Project Structure

```
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
│   └── (CSS, images, JS)
├── instance/
│   └── app.db
├── requirements.txt
└── README.md
```

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/20jyotiraditya04/FinSentiment-AI-Powered-Financial-News-Sentiment-Dashboard.git
cd FinSentiment
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

```bash
$Env:FLASK_APP = "app.py"
$Env:FLASK_ENV = "development"
```

### 5️⃣ Initialize the Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6️⃣ Run the App

```bash
flask run
```

> Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 💡 Inspiration

* **Yahoo Finance**
* **Bloomberg Terminal**
* **FinViz**

---

## 📈 Roadmap

* ✅ User authentication
* ✅ Live news aggregation + sentiment analysis
* ✅ Interactive stock price charts and fundamentals
* ✅ Sector/peer sentiment comparison
* ✅ AI-generated summaries & risk insights
* 🔜 User watchlists & alerts
* 🔜 Dark mode toggle
* 🔜 More advanced charting & data sources

---

## 🤝 Contributing

Pull requests are welcome!
Please open an issue first to discuss major changes.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* HuggingFace Transformers
* NLTK
* Plotly
* Bootstrap
* Animate.css
* Yahoo Finance (UI inspiration)

---

> Built with ❤️ by **Jyotiraditya**

---

## 📝 Project Overview

**FinSentiment** is an AI-powered web dashboard for analyzing financial news and stock sentiment.  
Key features include:

- **User Authentication:** Secure registration and login for personalized dashboards.
- **Live News Aggregation:** Fetches the latest financial/business news headlines.
- **NLP Enrichment:** Extracts entities and keywords from news using spaCy.
- **Sentiment Analysis:** Uses NLTK VADER and FinBERT to analyze news sentiment (positive/negative/neutral).
- **AI Summaries & Insights:** Generates concise news summaries and trend/risk insights using transformer models.
- **Stock Data Visualization:** Displays interactive 5-year stock price charts and key fundamentals using yfinance and Plotly.
- **Sector Comparison:** Compares sentiment of selected stock with its sector peers.
- **Filtering:** Allows filtering news by ticker, sentiment, and keyword.
- **Per-News Insights:** For each news, shows summary, affected stocks, conclusion, and actionable advice.
- **Modern UI:** Responsive, animated interface using Bootstrap 5 and Animate.css.

The project combines real-time data, NLP, and AI to help users quickly understand market sentiment and make informed decisions.

---

Let me know if you'd like a PDF or styled HTML version as well!
