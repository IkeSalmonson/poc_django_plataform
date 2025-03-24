from django.db import models
#-  manager => Name, email , contact, registered_providers 
# - service_provider => Name, email, contact, service_type, cost_estimate, region
# Create your models here.

class Service_provider(models.Model):
    def __str__(self):
        return self.name+self.service_type

    REGION = { 
            'R1':'region_1',
            'R2':'region_2',
            'R3' :'region_3',} 
    SERVICE_TYPE = {'P':'painter','B': 'bartender','B2':'bouncer'}
 
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=16)
    service_type = models.TextField(choices= SERVICE_TYPE, blank=True)
    cost_estimate = models.FloatField()
    region = models.TextField(choices=REGION, blank= True)

    class Meta:
        ordering = ['region']




#class manager(models.Model):
#    name 
#    email
#    contact 
#    registered_providers = models.Aggregate() 
