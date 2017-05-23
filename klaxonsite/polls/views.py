from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hey')

def sum(request, a, b):
    return HttpResponse('{0}+{1}={2}'.format(a,b,int(a)+int(b)))
    

# Create your views here.
