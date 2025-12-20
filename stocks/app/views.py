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

        def month_data_correction_for_chart(month_list):  # We use this to add every month amount with the previous one, and we can have a correct line in the chart.
            new_month_list=list()
            for i in range(len(month_list)):
                if i == 0:
                    new_month_list.append(month_list[i])
                else:
                    new_month_list.append(month_list[i] + new_month_list[i-1])
            return new_month_list



        total_data = result['chart']['total_value_list']
        month_data = result['chart']['monthly_amount_list']
        month_data = month_data_correction_for_chart(month_data)
        dates = result['chart']['dates']
        #dates = [d.strftime('%Y-%m-%d') for d in dates]

        fig, ax = plt.subplots()


        ax.plot(dates, total_data, linewidth=1, label='Total')
        ax.plot(dates, month_data, linewidth=1, label='Montly')

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


        # print(result)
        print(f'---monthly: {month_data}---')
        return render(request, 'app/index.html', context)
        

    return render(request, 'app/index.html')


