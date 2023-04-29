from django.shortcuts import render
from django.http import HttpResponse


def Catview(request):
    return HttpResponse('<h1>catregory view page</h1>')
def Single(request):
    return HttpResponse('<h1>single view page</h1>')
def Search(request):
    return HttpResponse('<h1>search page</h1>')