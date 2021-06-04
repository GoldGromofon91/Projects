### Фабрика решений

##### Требуемое окружение:
---
    Python==3.8.*
    Django==2.2.10
    djangorestframework==3.12.4
    pytz==2021.1
    sqlparse==0.4.1
---
##### Установка окружения и старт приложения:
  1. Для развертывания приложения необходимо установить [pyenv](https://github.com/pyenv/pyenv) или [virtualenv](https://github.com/pyenv/pyenv)
  (в зависимости от вашей среды разработки)
  1. Для развертывания приложения необходимо установить все зависимости. Для установки используйте команду `pip install -r requirements.txt`
  1. Для старта приложения перейдите в директорию `/server` в консоли используйте команду `python manage.py runserver`
---
##### Примеры:
  * Для проверки из строки браузера перейдите по:
      http://127.0.0.1:8000/admin/polls/,
      http://127.0.0.1:8000/admin/polls/1/,
      http://127.0.0.1:8000/admin/question/,
      http://127.0.0.1:8000/admin/question/1/,
      http://127.0.0.1:8000/admin/questionchoice/,
      http://127.0.0.1:8000/admin/questionchoice/2/,
      http://127.0.0.1:8000/active/,
      http://127.0.0.1:8000/detail/,
      http://127.0.0.1:8000/detail/1/
  * Для прохождения опроса необходимо воспользоваться примером из [файла](https://github.com/GoldGromofon91/Projects/blob/master/%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9/example.txt)
