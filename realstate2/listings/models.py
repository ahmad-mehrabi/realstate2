from django.db import models
from realtors.models import realtors
from datetime import datetime
class listings(models.model):
    realtor= models.ForeignKey(realtor, on_delete=models.DO_NOTHING(collector, field, sub_objs, using))
    title= models.CharField(max_length=150, blank=True)
    address= models.TextField()
    bathroom= models.IntegerField(default=1)
    bedroom= models.IntegerField(default=1)
    infr= models.CharField(max_length=30)
    details= models.TextField()
    is_published= models.BooleanField(default=True)
    list_date= models.DateTimeField(blank=True, default=datetime.now())
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title