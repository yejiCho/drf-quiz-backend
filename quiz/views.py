from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import  QuizSerialzier
import random

@api_view(['GET'])
def helloAPI(request):
    return Response('Hello World')

# 주어진 개수만큼 랜덤한 퀴즈를 반환한다.
@api_view(['GET'])
def randomQuiz(request,id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    serializer = QuizSerialzier(randomQuizs,many=True) 
    # many = True 다수의 데이터에 대해서도 직렬화가 진행됨
    return Response(serializer.data)

