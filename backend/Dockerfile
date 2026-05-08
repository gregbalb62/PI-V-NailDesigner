
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install django djangorestframework djangorestframework-simplejwt mysqlclient paho-mqtt gunicorn
CMD ["gunicorn","core.wsgi:application","--bind","0.0.0.0:8000"]
