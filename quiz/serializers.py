# 장고 모델데이터를 JSON타입으로 바꿔주는(직렬화) 코드
# 장고 모델 데이터를 템플릿에 뿌려주면 웹에서 보여지듯,
# JSON타입으로 뿌려주면 api로 통신이 되는 것이며
# 내 데이터를 JSON으로 바꿔주는 기계
from rest_framework import serializers
from .models import Quiz

# Quiz모델 데이터가 주어지면 title,body,answer를 포함한 JSON데이터로 변환해주는 시리얼라이저
class QuizSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title','body','answer') 
