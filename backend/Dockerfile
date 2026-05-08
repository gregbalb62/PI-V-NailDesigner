
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install django djangorestframework djangorestframework-simplejwt mysqlclient paho-mqtt
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
