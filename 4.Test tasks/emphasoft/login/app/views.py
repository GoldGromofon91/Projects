from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Users_reg

# from validate_email import validate_email
import re
import hashlib


def transformat(string,salt):
	hash_user_obj = hashlib.sha256(string.encode('ascii'))
	salt_hash = hashlib.sha224(salt.encode('ascii'))
	res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
	return res_pass



def login_usr(request):
	if request.method == "POST":
		email = request.POST.get('email','0')
		us_pass = transformat(request.POST.get('password','0'),email)
		try:
			user_objects = Users_reg.objects.get(email=email)
		except Users_reg.DoesNotExist:
			return redirect('/registration')
		else:
			return redirect('/index')
	else:
		return render(request, 'login.html')


def index(request):
	if request.method == "POST":
		return redirect('/all_users')
	return render(request, 'index.html')


def registration(request):
	if request.method == "POST":
		name_user = request.POST.get('user_name_reg','0')
		email = request.POST.get('user_email_reg','0')
		us_pass = request.POST.get('user_password_reg','0')
		match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
		# print(match)
		# print(f'Name-{name_user}, EMAIL-{email}, pass-{us_pass}')
		if match:
			hash_user_pass = transformat(us_pass,email) 
			add_usr = Users_reg(name=name_user,password=hash_user_pass,email=email)
			add_usr.save()
			return redirect('/login')
		else:
			return render(request, 'registration.html',{ 'error': 'Your email is not valid' })	
	else:		
		return render(request, 'registration.html')




def all_users(request):
	user_appeal = Users_reg.objects.all().order_by('-id','name')
	return render(request, 'all_users.html', context={'user_appeal': user_appeal})
	
