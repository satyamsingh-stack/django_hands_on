from django.db import models

# Create your models here.
class Items(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    barcode=models.IntegerField(unique=True)
