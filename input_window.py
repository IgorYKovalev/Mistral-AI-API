from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
import os
import sys


class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.question = None

    def init_ui(self):
        self.setWindowTitle('ТГ канал Python | Leetcode | Сodewars')
        self.setGeometry(400, 400, 400, 300)
        if getattr(sys, 'frozen', False):
            application_path = os.path.join(sys._MEIPASS, "Ава на ТГ канал.png")
        else:
            application_path = '/Users/kovalevigor/Desktop/Для постов/Ава на ТГ канал.png'

        layout = QVBoxLayout()

        image_label = QLabel(self)
        pixmap = QPixmap(application_path)
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(400, 300)

        label = QLabel('Напишите ваш вопрос:', self)
        self.input_field = QLineEdit(self)

        ok_button = QPushButton("OK", self)
        cancel_button = QPushButton("Отмена", self)

        ok_button.clicked.connect(self.ok_clicked)
        cancel_button.clicked.connect(self.close)

        layout.addWidget(image_label)
        layout.addWidget(label)
        layout.addWidget(self.input_field)
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)
        self.setLayout(layout)

    def ok_clicked(self):
        question = self.input_field.text()
        if not question:
            QMessageBox.warning(self, "Ошибка", "Вы не написали вопрос!", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Уведомление", "Ща подумаю и отвечу!", QMessageBox.Ok)
            self.question = question
            self.close()


def run_input_window():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = InputWindow()
    window.show()
    app.exec_()
    return window.question
