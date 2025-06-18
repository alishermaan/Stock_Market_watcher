# 🤖 AI Stock Market Watcher

An AI-powered terminal-based stock market agent that monitors live stock prices, analyzes sentiment from the news, classifies stocks as **Buy/Sell/Hold**, sends smart alerts, logs data, generates Excel charts, and emails a daily summary.

---

## 🚀 Features

* 📈 Live stock price tracking (using Yahoo Finance)
* 🧠 AI-based decision logic (rule-based using price & sentiment)
* 📰 News headline sentiment analysis (using VADER)
* 🔔 Smart alerts (only on significant price movements)
* 📊 Auto-generated Excel chart report
* 📤 Daily email summary
* 🎵 Sound + desktop notifications
* 💾 CSV + Excel export logging

---

## 📦 Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

### Python Dependencies

```
yfinance
beautifulsoup4
requests
nltk
rich
plyer
openpyxl
```

Also download the VADER lexicon:

```python
import nltk
nltk.download('vader_lexicon')
```

---

## 🧠 How It Works

1. Fetches stock prices and news headlines.
2. Analyzes sentiment using VADER.
3. Classifies each stock as:

   * 🟢 Buy (positive sentiment + low price)
   * 🔴 Sell (negative sentiment + high price)
   * 🟡 Hold (neutral or no trigger)
4. Alerts only on strong signals (crossing thresholds).
5. Displays data in a real-time terminal dashboard.
6. Logs to CSV/Excel and sends an optional email summary.

---

## 🛠 Usage

```bash
python ai_stock_agent.py
```

You'll be prompted to:

* Enter stock symbols (e.g., `AAPL, TSLA, GOOGL`) or use defaults
* Set refresh interval in seconds (e.g., `10`)

Press `Ctrl + C` to stop and trigger email + chart generation.

---

## 📧 Configure Daily Summary Email

Edit the following in `ai_stock_agent.py`:

```python
sender_email = "your_email@example.com"
sender_password = "your_password"
self.send_daily_summary_email("recipient@example.com")
```

> 🔐 Consider using environment variables or a `.env` file for security.

---

## 📂 Outputs

* `stock-market-prices.csv` — raw data log
* `stock_prices.xlsx` — spreadsheet with price data and charts
* Daily summary email (plain text list of buy/sell/hold actions)

---

## 📈 Screenshot (optional)

!\[screenshot of rich dashboard in terminal]

---

## ✨ Coming Soon

* Machine learning-based classification
* Web dashboard with historical charts
* Telegram bot alerts

---

## 📄 License

MIT License — free to use, share, and modify.

---

## 💬 Questions?

Open an issue or reach out on [GitHub](https://github.com/yourusername/ai-stock-agent).
