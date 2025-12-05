from django.shortcuts import render
from .models import Stocks, StocksHistory
import pandas as pd
import yfinance

# Create your views here.
def index(request):
    pass