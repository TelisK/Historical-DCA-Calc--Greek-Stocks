from django.shortcuts import render
from .models import Stocks, StocksHistory
from dateutil.relativedelta import relativedelta
from app.services.stock import stock_calculation
from datetime import date
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go



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
            asset='SXR8.DE',
            start_date=start_date,
            end_date=end_date,
            amount_per_month=amount_per_month,
            fixed_amount=fixed_amount
            )
        else:
            snp500 = None


        '''total_data = result['chart']['total_value_list']
        month_data = result['chart']['monthly_amount_list']
        dates = result['chart']['dates']
        dates = [d.strftime('%Y-%m-%d') for d in dates]

        trace1 = Scatter(x=dates, y=total_data, mode='lines+markers', name='Total Value',
                        opacity=0.8, marker_color='green',)
        trace2 = Scatter(x=dates, y=month_data, mode='lines+markers', name='Investment',
                        opacity=0.8, marker_color='red',)
        
        plot_div = plot([trace1, trace2], output_type='div')'''


        dates = [
                "2023-01-01",
                "2023-02-01",
                "2023-03-01",
                "2023-04-01",
            ]

        investment = [1000, 1200, 1300, 1500]
        profits = [0, 50, 120, 300]

        # 2️⃣ Δημιουργία γραμμών
        trace_investment = go.Scatter(
            x=dates,
            y=investment,
            mode="lines",
            name="Επένδυση"
        )

        trace_profits = go.Scatter(
            x=dates,
            y=profits,
            mode="lines",
            name="Κέρδη"
        )

        # 3️⃣ Layout (τίτλοι κτλ)
        layout = go.Layout(
            title="Επένδυση & Κέρδη",
            xaxis=dict(title="Ημερομηνία"),
            yaxis=dict(title="Ποσό (€)")
        )

        # 4️⃣ Φτιάχνουμε το figure
        fig = go.Figure(data=[trace_investment, trace_profits], layout=layout)

        # 5️⃣ Μετατροπή σε HTML (ΠΟΛΥ ΣΗΜΑΝΤΙΚΟ)
        plot_div = plot(fig, output_type="div", include_plotlyjs=False)





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


