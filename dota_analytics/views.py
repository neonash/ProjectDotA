from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'dota_analytics/index.html')

def prediction(request):
    return render(request, 'dota_analytics/Queue.html')
