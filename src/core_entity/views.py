#from django.http import HttpResponse
from django.shortcuts import render
from core_entity.models import Service_provider
from core_entity.forms import Service_provider_form
# Create your views here.
def index(request):
    context = {}
    form = Service_provider_form()
    service_providers = Service_provider.objects.all()
    context['service_providers'] = service_providers 
    context['title'] = 'UserTable'
    context['form'] = form
    return render(request, 'index.html', context)
    #return HttpResponse('Hello World! ')

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request,'about.html', context )    
