import base64
import io
from django.shortcuts import render
import urllib
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation
from datetime import date
from matplotlib import pyplot as plt
import matplotlib.dates as mdates


# Create your views here.
def index(request):
    if request.method == 'POST':
        asset = request.POST.get('asset','')
        fixed_amount = request.POST.get('initial', '')
        amount_per_month = request.POST.get('monthly', '')
        start_date = request.POST.get('startdate', '')
        end_date = request.POST.get('enddate','')
        
        #today = date.today()

        result = stock_calculation(
            asset=asset,
            start_date=start_date,
            end_date=end_date,
            amount_per_month=amount_per_month,
            fixed_amount=fixed_amount
        )

        compare = request.POST.get('compare') == 'on'

        if compare:
            snp500 = stock_calculation(
            asset='SXR8.DE',
            start_date=start_date,
            end_date=end_date,
            amount_per_month=amount_per_month,
            fixed_amount=fixed_amount
            )
        else:
            snp500 = None


        total_data = result['chart']['total_value_list']
        invested_data = result['chart']['invested_amount_list']
        dates = result['chart']['dates']


        fig, ax = plt.subplots()

        if compare:
            total_snp500_data = snp500['chart']['total_value_list']
            ax.plot(dates, total_data, linewidth=1, label='Total')
            ax.plot(dates, total_snp500_data, linewidth=1, label='S&P500')
            ax.plot(dates, invested_data, linewidth=1, label='Invested')
        else:
            ax.plot(dates, total_data, linewidth=1, label='Total')
            ax.plot(dates, invested_data, linewidth=1, label='Invested')

        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        ax.legend()
        ax.set_title('Investment Result')
        ax.set_xlabel('Years')
        ax.set_ylabel('Amount')
        ax.grid()

        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        string=base64.b64encode(buffer.read())
        url = urllib.parse.quote(string)



        context = {'summary':result['summary'],
                   'snp500':snp500,
                   'compare':compare,
                   'plot':url,
                   'snp500sum':snp500['summary'] if snp500 else None,
                   'snp500chart':snp500['chart'] if snp500 else None,
                   }



        return render(request, 'app/index.html', context)
        

    return render(request, 'app/index.html')


