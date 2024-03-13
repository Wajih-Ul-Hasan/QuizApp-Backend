from rest_framework.response import Response
from rest_framework import generics
from .serializers import QuizSerializer, RandomQuestionSerializer , QuestionSerializer
from .models import Question, Quizzes
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    @staticmethod
    def get(request,**kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
    

class QuizQuestion(APIView):
    @staticmethod
    def get(request,**kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)