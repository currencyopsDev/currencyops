import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import mplcursors

def get_closing_prices(symbol, period="1d"):
    ticker = yf.Ticker(symbol)
    prices_data = ticker.history(period,interval="5m")
    sns.lineplot(data=prices_data["Close"])
    mplcursors.cursor(hover=True)
    sns.set_theme()
    plt.xticks(rotation=30)
    plt.title(f"Closing Stock Prices for {ticker}")
    plt.show()    