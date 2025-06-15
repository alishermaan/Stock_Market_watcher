import yfinance as yf
import time
from datetime import datetime

# Default list of popular stocks
DEFAULT_SYMBOLS = [
    "AAPL", "TSLA", "AMZN", "GOOGL", "MSFT", "NVDA", "META",
    "NFLX", "IBM", "INTC", "BABA", "BA", "JPM", "DIS", "ORCL",
    "PYPL", "ADBE", "PEP", "NKE", "KO"
]

def get_stock_price(symbols):
    print(f"\n📈 Stock Prices at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 70)
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            price = stock.info['regularMarketPrice']
            name = stock.info.get('shortName', 'Unknown')
            print(f"{symbol:<6} ({name}): ${price}")
        except Exception as e:
            print(f"⚠️ Error fetching {symbol}: {e}")
    print("-" * 70)

def stock_market_watcher(symbols, refresh_interval=10):
    try:
        while True:
            get_stock_price(symbols)
            time.sleep(refresh_interval)
    except KeyboardInterrupt:
        print("\n⛔ Exiting Stock Market Watcher")

if __name__ == "__main__":
    user_input = input(
        "Enter stock symbols separated by commas (or press Enter to use defaults): "
    ).strip()
    
    if user_input:
        symbols = [s.strip().upper() for s in user_input.split(",")]
    else:
        symbols = DEFAULT_SYMBOLS
    
    try:
        refresh_interval = int(input("Enter refresh interval in seconds (e.g., 10): "))
    except ValueError:
        refresh_interval = 10
        print("⚠️ Invalid input. Using default interval: 10 seconds.")
    
    stock_market_watcher(symbols, refresh_interval)
# This script fetches and displays stock prices for a list of symbols.
# It allows users to input their own symbols or use a default list. 
# The prices are refreshed at a specified interval, and the script can be stopped with Ctrl+C.
