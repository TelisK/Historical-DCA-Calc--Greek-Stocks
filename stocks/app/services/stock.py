import pandas as pd
import yfinance
from app.models import Stocks, StocksHistory
import numpy as np  
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def stock_calculation(asset: str, start_date, end_date, amount_per_month, fixed_amount):
    #stock = yfinance.Ticker("AETF.AT")
    stock = yfinance.Ticker(asset)
    info = stock.info
    history = stock.history(period="max")
    df = pd.DataFrame(history)
    df = df.reset_index() # Περνάμε το date απο index σε column και δημιουργουμε indexes με αριθμους
    df['Date'] = pd.to_datetime(df['Date']) # Make it datetime form
    df['Date'] = df['Date'].dt.tz_localize(None) # Remove GMT

    #startdate = datetime(2023, 1, 1)
    #enddate = datetime(2024, 4, 1)
    #monthly_amount = 100
    startdate = datetime.strptime(start_date, '%Y-%m-%d')
    enddate = datetime.strptime(end_date, '%Y-%m-%d')
    monthly_amount = float(amount_per_month)
    monthly_amount_list = []
    dividend = 0
    date = startdate
    dates = []
    invested_amount = 0
    invested_amount_list = []
    total_value = 0
    total_value_list = []
    profit = 0
    total_shares = 0

    while enddate > date:
        mask = df['Date'] == date  # returns True at the position date is. Afterwards we use mask to locate the date.

        if not df.loc[mask].empty:
            close_price = df.loc[mask].Close.iloc[0]
        else:
            date = df[df['Date'] > date].iloc[0]['Date']
            mask = df['Date'] == date
            close_price = df.loc[mask].Close.iloc[0]


        if total_shares == 0 and fixed_amount:
            try:
                total_shares = float(fixed_amount) / float(close_price)
                total_value = total_shares * close_price
                total_value_list.append(total_value)
                invested_amount += float(fixed_amount)
                invested_amount_list.append(invested_amount)
                dates.append(date)
            except (ZeroDivisionError):
                print('+++++ERROR++++++')
                continue

        shares = monthly_amount / close_price
        total_shares += shares
        total_value = total_shares * close_price
        total_value_list.append(total_value)
        monthly_amount_list.append(monthly_amount)

        dividend = dividend + df.loc[mask].Dividends.iloc[0]
        invested_amount += monthly_amount
        invested_amount_list.append(invested_amount)

        dates.append(date)
        date = date + relativedelta(months=1)

    profit = total_value - invested_amount
    total_amount = invested_amount + profit
    pow_calc = 1/(len(dates)/12) # using len of dates to find the years
    annual_return = ((np.power((total_amount / invested_amount), pow_calc)) -1 ) * 100

    result = {
        'summary':{
        'total_investment':invested_amount,
        'annualized_return': annual_return,
        'shares': total_shares,
        'profit': profit,
        'dividend': dividend,
        'total_amount': total_amount,

    },
    'chart':{
        'total_value_list': total_value_list,
        'invested_amount_list': invested_amount_list,
        'dates': dates
    }
    }
        
    return result

