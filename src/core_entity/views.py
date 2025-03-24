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
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save') 
            if not pk: 
                form = Service_provider_form(request.POST)
 
            else: 
                service_provider = Service_provider.objects.get(id=pk)
                form = Service_provider_form(request.POST, instance=service_provider)
            form.save()
            form = Service_provider_form()


        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            service_provider = Service_provider.objects.get(id=pk)
            form = Service_provider_form(instance=service_provider)
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            service_provider = Service_provider.objects.get(id=pk)
            service_provider.delete()
             
    context['form'] = form
    return render(request, 'index.html', context)
    #return HttpResponse('Hello World! ')

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request,'about.html', context )    
