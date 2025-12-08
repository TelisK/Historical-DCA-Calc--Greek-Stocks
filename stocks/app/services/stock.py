import pandas as pd
import yfinance
from app.models import Stocks, StocksHistory



def stock_calculation(name):
    stock = yfinance.Ticker(name)
    stock_history = stock.history(period="max", interval="1d")

    df = pd.DataFrame(stock_history)
    # with reset index, date goes to a column and we have numbers for indexes
    df = df.reset_index()
    # removing the hours from the date and the gmt
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    stock_obj, created = Stocks.objects.get_or_create(name=name)
    if created:
        print(f"Δημιουργήθηκε νέο Stock: {name}")

    for row in df.itertuples():
        StocksHistory.objects.create(
            stock_id = stock_obj,
            date = row.Date,
            close = row.Close,
            dividends = row.Dividends
        )
        
        
        

# stock_calculation('AETF.AT')



'''    db_stock_name = 
    if Stocks.objects.get(stock_name) == stock_name:
        if Stocks.objects.get('last_updated') >= end_date:
'''