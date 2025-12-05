'''    # ο χρηστης θα βάζει την ημερομηνία εκκινησης και τερματισμού, η εφαρμογή θα πρέπει να βρει την
    #ημερομηνία και να συνεχισει καθε μηνα να προσθετει το ποσο που θελουμε
    stock_name = "AETF.AT"
    stock = yfinance.Ticker(stock_name) #πρεπει να περάσω μεταβλητή
    stock_history = stock.history(start=2023-12-11, end=2025-12-5) #πρεπει οι ημερομηνίες να είναι μεταβλητές
    # Check if stock exists
    db_stock_name = 
    if Stocks.objects.get(stock_name) == stock_name:
        if Stocks.objects.get('last_updated') >= end_date:
            return result ###

    
    else:  ###
        pass  ###'''

def stock_calculation(name):
    pass