from datetime import datetime
import time

import requests

"""
    Файл reciever.py - имитирует клиента который получает сообщения от клиента кто что-то отправляет 
    отправляет на сервер 

"""


def wrap_message(mess_obj):
    dt = datetime.fromtimestamp(mess_obj['time'])
    dt_to_str = dt.strftime('%H:%M:%S')
    print(mess_obj['name'], dt_to_str)
    print(mess_obj['text'])
    print()


after = 0.0
while True:
    mess_obj = requests.get('http://127.0.0.1:5000/views', params={'after': after}).json()
    for mess in mess_obj['message']:
        wrap_message(mess)
        if mess['text'] == 'about':
            print(f'Hello {mess["name"]}\n')
        elif mess['text'] == 'time':
            print(f"Current.time{datetime.now()}")
        elif mess['text'] == 'timeU':
            print(f"Времени с 1970 года прошло: {time.time()}")
        after = mess['time']
    time.sleep(1)
