from django.http import HttpResponse
from django.shortcuts import render, redirect
from my_blog.settings import PUBLISH_PASS
from . models import Publication,Comment,UserListFB

import datetime


def index(request):
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'POST':
    	user = request.POST.get('user_fb','')
    	email = request.POST.get('email_fb','')
    	body = request.POST.get('text_fb','')

    	if not user or not email or not body:
    		return render(request, 'list_user_fb.html', {'error':'Есть пустое поля'})
    
    	user_FB = UserListFB(user_fb=user, email_fb=email,text_fb=body)
    	user_FB.save()
    	return redirect('/')
    else:
    	return render(request,'contacts.html')


def listFB(request):
	user_appeal = UserListFB.objects.all()
	return render(request, 'list_user_fb.html', context={'user_appeal': reversed(user_appeal)})
	

def blog(request):
	publication_objects = Publication.objects.all()
	return render(request, 'blog.html', context={'publications': reversed(publication_objects)})


def publication(request,id_publ):
	try:
		publication_objects = Publication.objects.get(id=id_publ)
	except Publication.DoesNotExist:
		return redirect('/blog')
	
	comment = Comment.objects.filter(publication=id_publ)

	if request.method == "POST":
		author = request.POST.get('author_comment','')
		body_comm = request.POST.get('text_comment','')
		if  author and body_comm:
			publication_objects.comment_set.create(publication=id_publ, author_name = author, text_comment = body_comm)
			return redirect('/publication/' + str(publication_objects.id))
			render(request, 'publication.html', context={'publications':publication_objects, 'comments_user': reversed(comment)})
		else:
			return render(request, 'publication.html', context={'publications':publication_objects, 'comments_user': comment , 'error':'Есть пустое поля'})
	else:	
		return render(request, 'publication.html', context={'publications':publication_objects, 'comments_user': reversed(comment)})


def publish(request):
	if request.method == 'POST':
		title = request.POST.get('title','')
		text = request.POST.get('text','')
		password = request.POST.get('password','')

		if not password or not title or not text:
			return render(request, 'publish.html', {'error':'Есть пустое поля'})
		if password != PUBLISH_PASS:
			return render(request, 'publish.html',{'error':'Неправильный пароль'})
		
		publish = Publication(title=title, text=text)
		publish.save()

		return redirect('/publication/'+ str(publish.id))
	else:
		return render(request, 'publish.html')





















