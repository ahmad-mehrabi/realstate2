from django.db import models

class realtors(models.Model):
    name= models.CharField(max_length=150 , blank=True)
    phone= models.CharField(max_length=15, blank=True)
    address= models.TextField(blank=True)
    email=models.CharField(max_length=200, blank=True)
    facebook= models.CharField(max_length=200, blank=True)
