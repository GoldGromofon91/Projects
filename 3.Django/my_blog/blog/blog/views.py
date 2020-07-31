from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello from Django! (Главная страница)</h1><br><a href='/contacts'>Контакты</a><br><a href='/blog'>Блог</a>")


def contacts(request):
    return HttpResponse("<h1>Контакты</h1><p>Email: django@skill.com, phone:+79999995555 </p> <a href='/'>На главную</a>")


def blog(request):
    return HttpResponse("<h1>Мой блог</h1><h3>Меню блога</h3> <a href='/'>На главную</a>")
