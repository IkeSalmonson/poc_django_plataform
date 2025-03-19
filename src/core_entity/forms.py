from django import forms
from core_entity.models import Service_provider

class Service_provider_form(forms.ModelForm):
    class Meta:
        model = Service_provider
        fields = ['name','email','contact' ,'service_type' ,'cost_estimate' ,'region' ]

