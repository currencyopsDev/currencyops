import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import mplcursors


def get_closing_prices(symbol, period="1m"):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period)
        return data["Close"]
    except Exception as e:
        print("Failed to get required data.", e)



ticker = "USD"
period = "1y"

prices_data = get_closing_prices(ticker, period)
sns.lineplot(data=prices_data)
mplcursors.cursor(hover=True)
sns.set_theme()
plt.xticks(rotation=30)
plt.title(f"Closing Stock Prices for {ticker}")
plt.show()