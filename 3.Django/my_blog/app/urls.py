from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('contacts',views.contacts),
    path('blog',views.blog),
	path('publication/<int:id_publ>',views.publication),
	path('publish', views.publish),
	path('listFB', views.listFB)
    ]