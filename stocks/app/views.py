from django.shortcuts import render
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation



# Create your views here.
def index(request):
    if request.method == 'POST':
        asset = request.POST.get('asset','')
        fixed_amount = request.POST.get('initial', '')
        amount_per_month = request.POST.get('monthly', '')
        start_date = request.POST.get('startdate', '')
        end_date = request.POST.get('enddate','')
        
        result = stock_calculation(
            asset=asset,
            start_date=start_date,
            end_date=end_date,
            amount_per_month=amount_per_month,
            fixed_amount=fixed_amount
        )
        print(result)
        return render(request, 'app/index.html',{'result':result})
        

    return render(request, 'app/index.html')



    


'''def show_results(request, date):
    if request.method == 'POST':
        asset = request.POST.get('asset','')
        initial = request.POST.get('initial', '')
        monthly = request.POST.get('monthly', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate','')

        


    stock_calculation(asset)
    data = StocksHistory.objects.get(name=asset)
    
    if startdate == '':
        pass # επεστρεψε να περασει ημερομηνία
    else:
        start_date_obj = datetime.strptime(startdate, "%Y-%m-%d").date()
        end_date_obj = datetime.strptime(enddate, "%Y-%m-%d").date()
        while next_month < end_date_obj:

            next_month = start_date_obj + relativedelta(month=1)'''
