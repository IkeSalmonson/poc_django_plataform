#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('Hello World! ')

def about(request):
    return render(request,'about.html' )    
