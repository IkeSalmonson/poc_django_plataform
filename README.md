# Django CRUD
This repository contains dockerized DJANGO project for a plataform where Admins register service providers. <br>
Admin users register all other roles.<br>


## Comands to start up the project 
  Project requirements for locally installed tools:    <br>
    - Docker    
 
# Development

 To build a development Docker Image:
```
docker build -t 'django_plataform:dev'  .   
```

 Running develpment image on local volume: 
```
docker run -it -p 8000:8000 -v $(pwd)/src:/usr/share/src django_plataform:dev sh
```

Run server (container broadcast to localhost:8000)
```
python manage.py runserver 0.0.0.0:8000
```
Access on browser via: http://localhost:8000/

Admin Panel: http://localhost:8000/admin

Admin credentials: admin_user / admin_user


# References 
Run inside the container.
Commands: 
```
django-admin startproject django_plataform
```
```
django-admin startapp core_entity
```
```
 python manage.py createsuperuser
``` 
  Login and password: admin_user

## Specification 

### Entities data models
Importante atributes: <br>
 - service_provider => Name, email, contact, service_type, cost_estimate, region

## Page>/ CRUD service providers by admin on the plataform 
- [x]  Frontend
  - [x] Register User Page
   - [x] New User form
        - [x] input validation for fields

- [x] Backend
    - [x] Create Migration with tabel user
    - [x] Create API CRUD user

# Reference
[YT Django CRUD Tutorial by Tony Teach Tech](https://www.youtube.com/watch?v=SLTXTG6ZXIM&list=PL_vyuxE-AO-D0Fg-0DyHbekAXOYgRYlWA) <br>
[Repo Django CRUD by TonyFlo](https://github.com/tonyflo/django-crud)
