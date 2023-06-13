from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello')
# Create your views here.

def home(request):

    return render(request,'myapp/home.html')
