from django.shortcuts import render
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation
from datetime import date
from plotly.offline import plot
from plotly.graph_objs import Scatter




# Create your views here.
def index(request):
    if request.method == 'POST':
        asset = request.POST.get('asset','')
        fixed_amount = request.POST.get('initial', '')
        amount_per_month = request.POST.get('monthly', '')
        start_date = request.POST.get('startdate', '')
        end_date = request.POST.get('enddate','')
        
        '''today = date.today()'''

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
            asset='VUAA.DE',
            start_date=start_date,
            end_date=end_date,
            amount_per_month=amount_per_month,
            fixed_amount=fixed_amount
            )
        else:
            snp500 = None


        total_data = result['chart']['total_value_list']
        month_data = result['chart']['monthly_amount_list']
        dates = result['chart']['dates']
        dates = [d.strftime('%Y-%m-%d') for d in dates]

        trace1 = Scatter(x=dates, y=total_data, mode='lines+markers', name='Total Value',
                        opacity=0.8, marker_color='green',)
        trace2 = Scatter(x=dates, y=month_data, mode='lines+markers', name='Investment',
                        opacity=0.8, marker_color='green',)
        
        plot_div = plot([trace1, trace2], output_type='div')





        context = {'summary':result['summary'],
                   'snp500':snp500,
                   'compare':compare,
                   ''''today':today,'''
                   ''''chart': result['chart'],'''
                   'plot_div':plot_div,
                   'snp500sum':snp500['summary'] if snp500 else None,
                   'snp500chart':snp500['chart'] if snp500 else None,
                   }


        # print(result)
        print(f'---Ημερομηνίες: {type(dates[0])}---')
        print(plot_div[:500])
        return render(request, 'app/index.html', context)
        

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
