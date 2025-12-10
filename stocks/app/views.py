from django.shortcuts import render
from .models import Stocks, StocksHistory
from services.stock import stock_calculation
import datetime


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def show_results(request, date):
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

