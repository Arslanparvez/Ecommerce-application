from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    CAT=((1,'mobile'),(2,'shoes'),(3,'clothes'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.FloatField()
    pdetails=models.CharField(max_length=100,verbose_name="product Details")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name="Availabe")
    pimage=models.ImageField(upload_to='image')

class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)

class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)

