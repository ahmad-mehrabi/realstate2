from django.shortcuts import render
from django.http import HttpResponse


def Indexview(request):
    return HttpResponse('<h1>this is index page</h1>')
def Aboutview(request):
    return HttpResponse('<h1>this is about page</h1>')