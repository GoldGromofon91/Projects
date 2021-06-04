from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import AdminPollViewSet, AdminQuestionViewSet, AdminQuestionChoiceViewSet, UserActivePollViewSet, \
    QuestionAnswer, UserDetailViewSet

app_name = "polls"

admin_poll_list = AdminPollViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

admin_poll_change = AdminPollViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

admin_question_list = AdminQuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

admin_question_change = AdminQuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

admin_questionchoice_list = AdminQuestionChoiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

admin_questionchoice_change = AdminQuestionChoiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_active_poll_list = UserActivePollViewSet.as_view({
    'get': 'list',
})

user_detail_list = UserDetailViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('admin/polls/', admin_poll_list),
    path('admin/polls/<int:pk>', admin_poll_change),
    path('admin/question',admin_question_list),
    path('admin/question/<int:pk>',admin_question_change),
    path('admin/questionchoice', admin_questionchoice_list),
    path('admin/questionchoice/<int:pk>', admin_questionchoice_change),
    path('active/', user_active_poll_list),
    path('poll/', QuestionAnswer.as_view()),
    path('detail/',user_detail_list),
    path('detail/<int:pk>',user_detail_list),
]
