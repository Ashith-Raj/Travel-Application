from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Hotels(models.Model):
    hname = models.CharField(max_length=100) 
    himageb = models.ImageField(upload_to='images')
    hlocation = models.TextField()
    hrating = models.FloatField()
    hprice = models.FloatField()
    hdesc = models.TextField()

class Restuarants(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images')
    location = models.TextField()
    rating = models.FloatField()
    desc = models.TextField()

class Tourpackages(models.Model):
    name = models.CharField(100)
    image = models.ImageField(upload_to='images')
    location = models.TextField()
    desc = models.TextField()
    price = models.FloatField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    email = models.EmailField()
    Address = models.TextField()
    date = models.DateField()


