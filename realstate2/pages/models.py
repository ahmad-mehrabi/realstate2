from django.db import models

class about(models.Model):
    title= models.CharField(max_length=100, blank=True)
    text_body= models.TextField(blank=True)