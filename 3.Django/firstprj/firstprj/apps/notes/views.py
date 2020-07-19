from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Note
from django.utils import timezone
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def index(request):
	notes_list = Note.objects.order_by('-pub_date')
	return render(request, 'notes/list.html',{'notes_list':notes_list})

def detail(request,note_id):
	try:
		a = Note.objects.get(id = note_id)
	except:
		raise Http404("Такой заметки нет")

	return render(request, 'notes/detail.html',{'note': a})

def create_note(request):
	Note.objects.create(category_note = request.POST['category'],text_note = request.POST['text'],pub_date = timezone.now())
	return redirect(request.META.get('HTTP_REFERER'))

def delete_note(request,note_id):
	del_= Note.objects.get(id = note_id)
	del_.delete()	
	return redirect('notes:index')

def change_note(request,note_id):
	ch = Note.objects.get(id = note_id)
	ch.category_note = request.POST['category']
	ch.text_note = request.POST['text']
	ch.status_note = request.POST['status']
	ch.pub_date = timezone.now()
	ch.save()
	return redirect(request.META.get('HTTP_REFERER'))
	# return render(request, 'notes/detail.html',{'note': ch})

def back(request):
	return redirect('notes:index')


def check(request):
	return redirect(request.META.get('HTTP_REFERER'))


