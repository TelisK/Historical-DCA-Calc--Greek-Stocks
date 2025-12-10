import pandas as pd
import yfinance
from app.models import Stocks, StocksHistory

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



stock = yfinance.Ticker("AETF.AT")
info = stock.info
history = stock.history(period="2y")
df = pd.DataFrame(history)
df = df.reset_index() # Περνάμε το date απο index σε column και δημιουργουμε indexes με αριθμους
df['Date'] = pd.to_datetime(df['Date']) # Το κάνουμε τυπου datetime
df['Date'] = df['Date'].dt.tz_localize(None) # Αφαιρούμε το gmt

startdate = datetime(2023, 1, 1)
enddate = date = datetime(2024, 4, 1)
monthly_amount = 100
dividend = 0
date = startdate
dates = []
invested_amount = 0
total_value = 0
profit = 0
#previous_close_price = 0
total_shares = 0
while enddate > date:
    mask = df['Date'] == date
    if not df.loc[mask].empty:
        close_price = df.loc[mask].Close.iloc[0]
    else:
        date = df[df['Date'] > date].iloc[0]['Date']
        mask = df['Date'] == date
        close_price = df.loc[mask].Close.iloc[0]
    print(f'τιμή {close_price}')
    shares = monthly_amount/close_price
    total_shares += shares
    print(f'αριθμός μετοχών {total_shares}')
    if previous_close_price == 0:
        total_value = monthly_amount
    else:
        total_value = total_shares * close_price
    #previous_close_price = close_price
    dividend = dividend + df.loc[mask].Dividends.iloc[0]
    invested_amount += monthly_amount
    profit += total_value - invested_amount
    dates.append(date)
    date = date + relativedelta(months=1)
print(f'Επένδυσες {invested_amount}, έχεις σύνολο {profit + invested_amount}, κέρδος {profit}. Τα μερίσματα σου είναι {dividend}, αγόρασες {total_shares} μετοχές')




'''
def stock_calculation(asset):
    stock = yfinance.Ticker(asset)
    stock_history = stock.history(period="max", interval="1d")

    df = pd.DataFrame(stock_history)
    # with reset index, date goes to a column and we have numbers for indexes
    df = df.reset_index()
    # removing the hours from the date and the gmt
    df['Date'] = pd.to_datetime(df['Date']).dt.date


    stock_obj, created = Stocks.objects.get_or_create(name=asset)
    if created:
        print(f"Δημιουργήθηκε νέο Stock: {asset}")

    for row in df.itertuples():
        StocksHistory.objects.create(
            stock_id = stock_obj,
            date = row.Date,
            close = row.Close,
            dividends = row.Dividends
        )'''

# def date_check(asset,date):
#         if dt.now() > date:
#             stock_calculation(asset)


# def get_or_create(name):
        
#         if name in Stocks.objects.get('name'):
#             date_check(name)
#         else:
             
        

# stock_calculation('AETF.AT')



'''    db_stock_name = 
    if Stocks.objects.get(stock_name) == stock_name:
        if Stocks.objects.get('last_updated') >= end_date:
'''