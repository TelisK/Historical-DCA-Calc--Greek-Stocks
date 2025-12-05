from django.db import models

# Create your models here.
# Making a hybrid model, which will work through database and realtime, depending the updated data.
class Stocks(models.Model):
    name = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StocksHistory(models.Model):
    date = models.DateTimeField()
    close = models.FloatField()
    dividends = models.FloatField()
    stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.stock_id.name} -->  {self.close[-1]}'

