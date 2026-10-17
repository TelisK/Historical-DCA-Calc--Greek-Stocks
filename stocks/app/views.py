import base64
import io
from django.shortcuts import render, redirect
import urllib
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation
from datetime import date
import plotly.express as px
from django.contrib import messages
# from matplotlib import pyplot as plt
# import matplotlib.dates as mdates


# Create your views here.
def index(request):

    ASSETS = {
    'AETF.AT':'ALPHA ETF FTSE (AETF.AT)',
    'AIA.AT':'Athens International Airport S.A. (AIA.AT)',
    'OPAP.AT':'Organization of Football Prognostics S.A. (OPAP.AT)',
    'EUROB.AT':'Eurobank Ergasias Services and Holdings S.A. (EUROB.AT)',
    'EEE.AT':'Coca-Cola HBC AG (EEE.AT)',
    'ETE.AT':'National Bank of Greece S.A. (ETE.AT)',
    'TPEIR.AT':'Piraeus Financial Holdings S.A. (TPEIR.AT)',
    'ALPHA.AT':'Alpha Bank S.A. (ALPHA.AT)',
    'MTLN.AT':'Metlen Energy & Metals PLC (MTLN.AT)',
    'HTO.AT':'Hellenic Telecommunications Organization S.A. (HTO.AT)',
    'PPC.AT':'Public Power Corporation S.A. (PPC.AT)',
    'BELA.AT':'Jumbo S.A. (BELA.AT)',
}
    
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
        if result == None:
            messages.error(request, 'Something went wrong. Check the dates')
            context = {
                'form_data': request.POST if request.method == 'POST' else {},
                'ASSETS':ASSETS,
            }
            return render(request, 'app/index.html', context)

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

        if compare:
            total_snp500_data = snp500['chart']['total_value_list']
            if len(total_snp500_data) != len(total_data):
                messages.error(request, "The stocks dates don't fit. Please select different dates.")
                
                context = {
                    'form_data': request.POST if request.method == 'POST' else {},
                    'ASSETS':ASSETS,
                }
                return render(request, 'app/index.html', context)
            else:
                investment_fig = px.line(
                    {'Years':dates, 'Contributions':invested_data,
                    'Contributions & Gains':total_data, 'S&P500': total_snp500_data},
                    x='Years',
                    y=['Contributions & Gains', 'Contributions', 'S&P500'],
                    title='Investment Result',
                    labels={'dates':'Years', 'value':'Amount','variable':''}
                )
    
        else:
            investment_fig = px.line(
                {'Years':dates, 'Contributions':invested_data, 'Contributions & Gains':total_data},
                x='Years',
                y=['Contributions', 'Contributions & Gains'],
                title='Investment Result',
                labels={'dates':'Years', 'value':'Amount', 'variable':''}
                )
            
        investment_fig.update_layout(
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=30),  # margins for the chart
        font=dict(size=10),                     # smaller font
        title=dict(font=dict(size=12)),     # smaller title font size
        legend_title_text='',     # removes the word variable from legend
        legend=dict(   # default orientation 'v', legend is on the right side of the chart.
        orientation='h') )

        investment_chart = investment_fig.to_html(include_plotlyjs=False, #We load plotly on html head
                        config={'responsive': True, 'displayModeBar': False},
                        full_html=False)

        # fig, ax = plt.subplots()

        # if compare:
        #     total_snp500_data = snp500['chart']['total_value_list']
        #     ax.plot(dates, total_data, linewidth=1, label='Total')
        #     ax.plot(dates, total_snp500_data, linewidth=1, label='S&P500')
        #     ax.plot(dates, invested_data, linewidth=1, label='Invested')
        # else:
        #     ax.plot(dates, total_data, linewidth=1, label='Total')
        #     ax.plot(dates, invested_data, linewidth=1, label='Invested')

        # ax.xaxis.set_major_locator(mdates.YearLocator())
        # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        # ax.legend()
        # ax.set_title('Investment Result')
        # ax.set_xlabel('Years')
        # ax.set_ylabel('Amount')
        # ax.grid()

        # buffer = io.BytesIO()
        # fig.savefig(buffer, format='png')
        # buffer.seek(0)
        # string=base64.b64encode(buffer.read())
        # url = urllib.parse.quote(string)



        context = {'summary':result['summary'],
                   'ASSETS': ASSETS,
                   'snp500': snp500,
                   'compare': compare,
                   'asset': asset,
                   'investment_chart':investment_chart,
                #    'plot':url,
                   'snp500sum':snp500['summary'] if snp500 else None,
                #    'snp500chart':snp500['chart'] if snp500 else None,
                'form_data': request.POST if request.method == 'POST' else {},
                   }



        return render(request, 'app/index.html', context)
        
    context = {
        'form_data': request.POST if request.method == 'POST' else {},
        'ASSETS': ASSETS
    }
    return render(request, 'app/index.html', context)


