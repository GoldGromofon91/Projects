from django.urls import path

from . import views
# from . views import MyRegisterFormView


app_name = 'notes'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('create/', views.create_note, name = 'create'),
	path('<int:note_id>/', views.detail, name = 'detail'),
	path('<int:note_id>/delete/', views.delete_note, name = 'delete'),
	path('<int:note_id>/change/', views.change_note, name = 'change'),
	path('back/', views.back, name = 'back'),
	path('check/', views.check, name = 'check'),
]  
