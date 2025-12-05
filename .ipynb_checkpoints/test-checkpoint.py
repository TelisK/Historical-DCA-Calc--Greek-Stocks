import yfinance
import pandas as pd

stock = yfinance.Ticker("AETF.AT")
info = stock.info
history = stock.history(start=2023-12-11, end=2025-12-5)
df = pd.DataFrame(history)
print(df)

# ΒΑΛΕ ΣΥΓΚΡΙΣΗ ΜΕ VUAA, APPLE, GOOGLE 
# METHODS

# import yfinance as yf
# stock = yf.Ticker("AAPL")

# META

# Βασικές πληροφορίες εταιρείας
# stock.info

# Ιστορικά δεδομένα (παρελθόν)
# history = stock.history(period="1y")
# print(history)

# Options για period:
# "1d", "5d", "1mo", "3mo", "6mo"
# "1y", "2y", "5y", "10y"
# "ytd", "max"

# Live price (τρέχουσα τιμή)
# price = stock.history(period="1d")["Close"].iloc[-1]
# print(price)

# Dividends
# stock.dividends

# Financial statements
# stock.balance_sheet
# stock.cashflow
# stock.income_stmt

# ISIN (όπου υπάρχει)
# stock.isin

# Αναλυτές, συστάσεις
# stock.recommendations

# Πώς ψάχνεις ticker μέσω κώδικα;
# Υπάρχει ένα όμορφο trick:
# import yfinance as yf
# results = yf.search("Tesla")
# print(results)
