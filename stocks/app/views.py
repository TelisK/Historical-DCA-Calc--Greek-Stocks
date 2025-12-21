import base64
import io
from django.shortcuts import render
import urllib
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation
from datetime import date
<<<<<<< HEAD
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
=======
from plotly.offline import plot
from plotly.graph_objs import Scatter
import json
>>>>>>> fee1d8420f3eb2fafe04efadd5ddb94d5336ae4e




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


<<<<<<< HEAD


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
=======
        total_data = result['chart']['total_value_list']
        month_data = result['chart']['monthly_amount_list']
        dates = result['chart']['dates']
        dates = [d.strftime('%Y-%m-%d') for d in dates]

        # trace1 = Scatter(x=dates, y=total_data, mode='lines+markers', name='Total Value',
        #                 opacity=0.8, marker_color='green',)
        # trace2 = Scatter(x=dates, y=month_data, mode='lines+markers', name='Investment',
        #                 opacity=0.8, marker_color='red',)
        
        # plot_div = plot([trace1, trace2], output_type='div', include_plotlyjs=False, config={'responsive': True})
>>>>>>> fee1d8420f3eb2fafe04efadd5ddb94d5336ae4e

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



<<<<<<< HEAD
        context = {'summary':result['summary'],
                   'snp500':snp500,
                   'compare':compare,
                   'plot':url,
                   'snp500sum':snp500['summary'] if snp500 else None,
                   'snp500chart':snp500['chart'] if snp500 else None,
                   }


=======
        context = { 'summary':result['summary'],
                    'snp500':snp500,
                    'compare':compare,
                    ''''today':today,'''
                    ''''plot_div':plot_div,'''
                    'dates_json': json.dumps(dates),
                    'total_data_json': json.dumps(total_data),
                    'month_data_json': json.dumps(month_data),
                    'plot_exists': True,
                    'snp500sum':snp500['summary'] if snp500 else None,
                    'snp500chart':snp500['chart'] if snp500 else None,
                   }


        # print(result)
        print(f'---Ημερομηνίες: {type(dates[0])}---')
        # print(plot_div[:500])
>>>>>>> fee1d8420f3eb2fafe04efadd5ddb94d5336ae4e
        return render(request, 'app/index.html', context)
        

    return render(request, 'app/index.html')


