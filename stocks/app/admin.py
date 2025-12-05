from django.contrib import admin
from .models import Stocks, StocksHistory

# Register your models here.
admin.site.register(Stocks)
admin.site.register(StocksHistory)