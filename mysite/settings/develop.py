from .base import *


SECRET_KEY = 'django-insecure-#g$ln(c(e(3ua*(q9v^a-1(ug6h7eu#z5l@im51_cf*i$!yw3('
# Debug = True : 개발모드 , False : 운영모드
DEBUG = True
# ALLOWED_HOSTS 를 공백으로 놔두면 ['localhost', '127.0.0.1'] 인식한다.
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}