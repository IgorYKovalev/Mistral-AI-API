import os
import json
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QDesktopWidget
from mistralai import Mistral
from input_window import run_input_window


class MyApp(QWidget):
    def __init__(self, text):
        super().__init__()

        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, 'config.json')
        with open(config_path) as config_file:
            config = json.load(config_file)
            api_key = config["MISTRAL_API_KEY"]

        model = "mistral-large-latest"

        client = Mistral(api_key=api_key)

        if text and isinstance(text, str) and text.strip():
            chat_response = client.chat.complete(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": text,
                    },
                ]
            )
            self.log_message(chat_response.choices[0].message.content)
        else:
            self.show_message("Уведомление", "Всего хорошего!!!")


    def log_message(self, message):
        log_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "log.txt")
        with open(log_file_path, "a") as log_file:
            log_file.write(message + "\nПодписывайтесь на ТГ канал - Python | Leetcode | Сodewars\n\n")


    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)

        screen = QDesktopWidget().screenGeometry()
        size = msg_box.sizeHint()
        msg_box.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication([])
    text = run_input_window()
    window = MyApp(text)
    window.show()


# pyinstaller --onefile --noconsole --add-data "/Users/kovalevigor/Desktop/Для постов/Ава на ТГ канал.png:." --add-data "config.json:." --add-data "input_window.py:." gpt.py