import time
from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui


class CharlesWindowFunction(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self,server_url):
        super().__init__()
        self.setupUi(self)
        self.server_url = server_url

        self.send.pressed.connect(self.on_click)  # соединение сигнала и слота (сигнал clicked и слот on_click)
        """
        так как в receiver.py мы делали задержку через time.sleep() в QT за это отвечает функция таймер
        Определим переменную after- которая сначала равна 0, затем времени
        Последнего сообщения
        """
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_messages)
        self.timer.start(1000)

    def wrap_message(self, mess_obj):
        dt = datetime.fromtimestamp(mess_obj['time'])
        dt_to_str = dt.strftime('%H:%M:%S')
        self.all_messages.append(mess_obj['name'] + " " + dt_to_str)
        self.all_messages.append(mess_obj['text'])
        self.all_messages.append('')
        self.all_messages.repaint()

    # Метод подгрузки сообщений в фоновом режиме
    def load_messages(self):
        #Если сервер падает то и падает приложение, чтобы избежать обработаем исключение
        #Если сервер упал, функция load_messages просто закончит свое выполнение
        try:
            mess_obj = requests.get(self.server_url + '/views', params={'after': self.after}).json()
        except:
            return

        for mess in mess_obj['message']:
            self.wrap_message(mess)
            self.after = mess['time']

    # Метод отправки сообщений на сервер
    def on_click(self):
        name = self.us_name.text()
        text = self.us_text.toPlainText()

        data_obj = {'name': name, 'text': text}
        # Валидация при отправке неправильных сообщений
        try:
            response = requests.post(self.server_url + '/send', json=data_obj)
        except:
            self.all_messages.append('Сервер недоступен. Попробуйте позже\n')
            self.all_messages.repaint()
            return

        if response.status_code != 200:
            self.all_messages.append('Заполните все поля\n')
            self.all_messages.repaint()
            return

        self.us_text.setText('')
        self.us_text.repaint()

        # to fix painting:
        # self.some_element.repaint()


app = QtWidgets.QApplication([])
window = CharlesWindowFunction('http://127.0.0.1:5000')
window.show()
app.exec_()
