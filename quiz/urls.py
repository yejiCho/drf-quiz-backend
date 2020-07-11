# quiz_app의 url 관리
from django.urls import path,include
from .views import helloAPI,randomQuiz

urlpatterns = [
    path('hello/',helloAPI),
    path('<int:id>/',randomQuiz),
]