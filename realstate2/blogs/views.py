from django.shortcuts import render
from django.http import HttpResponse

def Blog_view (request):
    return HttpResponse('<h1>Blog</h1>')
def Single_view(request,id):
    return HttpResponse('<h1>post number:</h1>'+str(id))