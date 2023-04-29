from django.urls import path
from .views import Indexview,Aboutview

urlpatterns=[
    path('',Indexview,name='index'),
    path('about/',Aboutview,name='about'),
]