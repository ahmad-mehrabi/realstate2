from django.urls import path
from .views import Blog_view,Single_view

urlpatterns=[
    path('',Blog_view,name='blog'),
    path('<int:id>',Single_view, name='single')
]