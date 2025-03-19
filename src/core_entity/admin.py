from django.contrib import admin
from core_entity.models import Service_provider

# Register your models here.
class Service_provider_admin(admin.ModelAdmin):
    list_display = ['id', 'name','service_type' , 'region'  ]
admin.site.register(Service_provider,Service_provider_admin)

## service_type region 