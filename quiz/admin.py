from django.contrib import admin
from .models import Quiz

admin.site.register(Quiz)

# django-cors-headers cors 에러 방지
# gunicorn 배포를 위한 도구
# psycopg2-binary , dj-database-url은 Heroku에서 사용하는 DB인 postgresql을 위한 것
# whitenoise는 정적파일의 사용을 돕는 미들웨어입니다.