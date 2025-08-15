from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=50)
    miktar = models.IntegerField()

class StockHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)  
    quantity_added = models.IntegerField()  
    date_added = models.DateTimeField() 
    movements=models.CharField(max_length=50,default='eklendi')  
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
