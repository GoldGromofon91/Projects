"""
    Файл server.py -для работ на стороне сервера
    message - временный объект для храненния сообщений от пользователей
"""
from collections import Counter

from flask import Flask, request, Response
from datetime import datetime, timedelta
import random
import time

app = Flask(__name__)

message = []
author = []


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Status</a><br><a href='/views'>"


@app.route("/send", methods=['POST'])
def send():
    name = request.json.get('name')
    text = request.json.get('text')
    #Валидация входных значений
    if not name or not isinstance(name, str) or not text or not isinstance(text, str):
        return Response(status=400)

    if name in author:
        pass
    else:
        author.append(name)

    message.append({'name': name, 'time': time.time(), 'text': text})
    print(message)
    return Response(status=200)  # *

# *т.к. определил метод пост мы должны что-то возвращать в HTML. Иначе 405 либо 5хх

def sort_mess(message_obj, key, treshold):
    filtered = []
    for elem in message_obj:
        if elem[key] > treshold:
            filtered.append(elem)
    return filtered


@app.route("/views")
def views():
    #Валидация передаваемого параметра(на старнице views)
    #after - граница, сообщений по времени (передается в ручную)
    try:
        after = float(request.args['after'])
    except TypeError:
        return Response(status=400)

    filtered = sort_mess(message, key='time', treshold=after)
    print(filtered)
    return {'message': filtered}


@app.route("/status")
def status():
    return {'status': random.choice(['True', 'False']),
            'name': 'Charlse',
            'date': datetime.now(),
            'count_user': len(author),
            'count_message': len(message)
            }


# 1598776781.87585
app.run()
