import yfinance as yf
import time
from datetime import datetime
import csv
import os
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

console = Console()

# Default stock list
DEFAULT_SYMBOLS = [
    "AAPL", "TSLA", "AMZN", "GOOGL", "MSFT", "NVDA", "META",
    "NFLX", "IBM", "INTC", "BABA", "BA", "JPM", "DIS", "ORCL",
    "PYPL", "ADBE", "PEP", "NKE", "KO"
]

# CSV file name
CSV_FILE = "stock_prices.csv"

# For price change comparison
previous_prices = {}

# 🆕 Price Threshold Alerts
PRICE_THRESHOLDS = {
    "AAPL": {"min": 180, "max": 200},
    "TSLA": {"min": 150, "max": 250},
    "GOOGL": {"min": 100, "max": 150},
    # Add more if needed
}

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Symbol", "Name", "Price"])

def export_to_csv(timestamp, rows):
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow([timestamp] + row)

def build_table_and_csv(symbols):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = Table(title=f"📈 Live Stock Market Watcher | {timestamp}", box=box.SQUARE)
    table.add_column("Symbol", style="bold")
    table.add_column("Name")
    table.add_column("Price", justify="right")
    table.add_column("Change", justify="center")
    table.add_column("Alert", justify="left")

    csv_rows = []

    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            price = info['regularMarketPrice']
            name = info.get('shortName', 'Unknown')

            prev = previous_prices.get(symbol)
            if prev is None:
                change_text = "–"
                change_style = "white"
            elif price > prev:
                change_text = f"↑ {price - prev:.2f}"
                change_style = "green"
            elif price < prev:
                change_text = f"↓ {prev - price:.2f}"
                change_style = "red"
            else:
                change_text = "→ 0.00"
                change_style = "yellow"

            previous_prices[symbol] = price
            alert_text = ""

            # 🔔 Threshold Alert Logic
            thresholds = PRICE_THRESHOLDS.get(symbol)
            if thresholds:
                if price > thresholds.get("max", float("inf")):
                    alert_text = "[bold red]🔺 ABOVE MAX[/bold red]"
                elif price < thresholds.get("min", float("-inf")):
                    alert_text = "[bold blue]🔻 BELOW MIN[/bold blue]"

            table.add_row(symbol, name, f"${price:.2f}", f"[{change_style}]{change_text}[/{change_style}]", alert_text)
            csv_rows.append([symbol, name, price])

        except Exception as e:
            table.add_row(symbol, "⚠️ Error", "N/A", "–", str(e))

    export_to_csv(timestamp, csv_rows)
    return table

def stock_market_watcher_live(symbols, refresh_interval=10):
    init_csv()
    with Live(build_table_and_csv(symbols), refresh_per_second=1, screen=True) as live:
        try:
            while True:
                time.sleep(refresh_interval)
                live.update(build_table_and_csv(symbols))
        except KeyboardInterrupt:
            console.print("\n⛔ Exiting Live Ticker UI...", style="bold red")

if __name__ == "__main__":
    user_input = input(
        "Enter stock symbols separated by commas (or press Enter to use defaults): "
    ).strip()

    symbols = [s.strip().upper() for s in user_input.split(",")] if user_input else DEFAULT_SYMBOLS

    try:
        refresh_interval = int(input("Enter refresh interval in seconds (e.g., 10): "))
    except ValueError:
        refresh_interval = 10
        print("⚠️ Invalid input. Using default interval: 10 seconds.")

    stock_market_watcher_live(symbols, refresh_interval)
