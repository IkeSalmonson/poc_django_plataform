# Django CRUD and restricted access by user role 
    This repository contains dockerized DJANGO project for a plataform where users with different roles have access to differente resources. <br>


## Comands to start up the project 
  Project requirements for locally installed tools:    <br>
    - Docker    

### // To Do  First use
<br> 

 Create Docker Images locally :
```
docker compose build  
```
Setup backend dependencies and donwload files to local volume: 
```
docker run  -p 8000:8000  -v $(pwd):/var/www/html   'pocdjangoplataform:prod'  sh init.sh
```

### // To Do  To run containers
 To run all services after first time setup:
```
docker compose up 
```

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

Admin credentials: root 123123


# References 
Run inside the container.
Commands: 
```
django-admin startproject
```
```
python manage.py startapp
```
```
python manage.py migrate
```
```
python manage.py createsuperuser 
```

## Specification 
 
## Page>/register_user CRUD users register by admin on the plataform 
- [ ]  Frontend
  - [ ] Register User Page
   - [ ] New User form
        - [ ] input validation for fields
   - [ ] New User button

- [ ] Backend
    - [ ] Create Migration with tabel user
    - [ ] Create API CRUD user


## Page>/register_artist CRUD marcham register service provider page on the plataform 
- [ ]  Frontend
  - [ ] Register Service Provider Page
   - [ ] New artist form
        - [ ] input validation for fields
   - [ ] New service provider button

- [ ] Backend
    - [ ] Create Migration with tabel service_provider
    - [ ] Create API CRUD service provider

## Page>/service_provider/{id} shows service provider profile on the plataform 
- [ ]  Frontend
  - [ ] Profile page
   - [ ] information td 
   - [ ] contact artist button
   - [ ] request budget artist button
   - [ ] chat artist button

- [ ] Backend
    - [ ] Create API get service provider by id 
  
## Page>/search/{search terms} shows service provider profile that match search terms on the plataform 
- [ ]  Frontend
  - [ ] Search page
   - [ ] search terms input 
   - [ ] filter search options
   - [ ] information td 

- [ ] Backend
    - [ ] Create API search artist by atributes 
  
   