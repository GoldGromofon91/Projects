from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Poll, Question, QuestionChoice, Answer
from polls.serializer import PollSerializer, QuestionSerializer, QuestionChoiceSerializer, AnswerSerializer, \
    DetailSerializer

#Создание/редактирование/удаление опросов(только АДМИН)
class AdminPollViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

#Создание/редактирование/удаление вопросов(только АДМИН)
class AdminQuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#Создание/редактирование/удаление вариантов вопроса (только АДМИН)
class AdminQuestionChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = QuestionChoice.objects.all()
    serializer_class = QuestionChoiceSerializer

#Просмотр активных опросов
class UserActivePollViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Poll.objects.filter(visible=True)
    serializer_class = PollSerializer


class QuestionAnswer(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = AnswerSerializer

    def post(self, request):
        serializer = AnswerSerializer(data=request.data, context=request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'result': 'OK'})


class UserDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = DetailSerializer

    def get_queryset(self,pk=None):
        if self.kwargs.get('pk'):
            queryset = Poll.objects.filter(poll_to_answer__participant=self.kwargs.get('pk'),visible=True)
            return queryset
        else:
            queryset = Poll.objects.all()
            return queryset
