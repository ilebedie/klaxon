from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hey')

# Create your views here.
