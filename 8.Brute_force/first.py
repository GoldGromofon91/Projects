"""
Отправляем по 100 запросов на указанные урлы
"""
import requests
import datetime

urls = ['http://example.com',
        'https://geekbrains.ru',
        'https://github.com',
        'https://djbook.ru/rel3.0/#',
        'https://developer.mozilla.org/ru/docs/Learn/Server-side/Django',
        'https://html5css.ru',
        'https://medium.com/@ixr/настройка-zsh-в-mac-os-534e890028b8',
        'https://cloud.croc.ru/blog/byt-v-teme/flask-prilozheniya-v-docker/',
        ]


def easy_requests(at_urls, total=0, count=100, start=datetime.datetime.now()):
    for url in at_urls:
        print(f'Site:\t{url}')
        for i in range(count):
            response = requests.get(url)
            # print(response.status_code == 200)
            if response.status_code == 200:
                total += 1
                continue
            else:
                break
        print(f'site:{url}\tTime{(datetime.datetime.now() - start)}\tCount_success_connect:{total}')


if __name__ == '__main__':
    easy_requests(urls)
