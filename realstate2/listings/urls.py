from django.urls import path
from .views import Catview,Single,Search


urlpatterns=[
    path('cat/',Catview,name='catview'),
    path('singleview/',Single,name='singleview'),
    path('search/',Search,name='search'),
]