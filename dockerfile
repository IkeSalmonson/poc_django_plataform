FROM python:3.12.3-alpine3.19

WORKDIR /usr/share/src 

COPY  /requirements.txt    ./ 
EXPOSE 8000
RUN  pip install -r ./requirements.txt  

COPY /src/  ./