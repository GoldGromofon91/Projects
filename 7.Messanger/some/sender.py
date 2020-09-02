import requests

"""
    Файл sender.py - имитирует клиента который отправляет что-то на сервер
    
    Метод requests.get('url',param) Получить данные с урла 
    Параметр headers - какие заголовки вернул сервер, text - что отдал 
    пользователь(текст), json() - для преобразования ответа в словарь в Python
    
    print(requests.get('http://127.0.0.1:5000/status').headers)
    print(requests.get('http://127.0.0.1:5000/status').text)
    
    Метод requests.post('url', obj) - обращение к серверу и передача объектов на сервер; 
    встроенная функция json преобразует словарь в json затем в html затем отправляет на сервер
"""


# print(requests.get('http://127.0.0.1:5000/status').json())

def send():
    name = input('Введите имя: ')
    while True:
        text = input()
        if text == ',./':
            print('Bye')
        else:
            data_obj = {'name': name, 'text': text}
            requests.post('http://127.0.0.1:5000/send', json=data_obj)


if __name__ == "__main__":
    send()
