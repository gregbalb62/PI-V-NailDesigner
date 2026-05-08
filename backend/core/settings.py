
SECRET_KEY = 'secure'
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'iot',
  'USER': 'root',
  'PASSWORD': 'root',
  'HOST': 'db',
  'PORT': '3306'
 }
}
