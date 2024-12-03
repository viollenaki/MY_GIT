import requests
from PyQt5.QtWidgets import QAction, QMenu, QMessageBox, QDialog, QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from collections import defaultdict
import sys








class Registration(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)

        self.label = QLabel("NAME")
        self.username = QLineEdit()
        self.label2 = QLabel("PASSWORD")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton("Register")

        self.info_status = QLineEdit()
        self.info_status.setReadOnly(True)

        font = QFont()
        font.setPointSize(14) 

        self.label.setFont(font)
        self.username.setFont(font)
        self.label2.setFont(font)
        self.password.setFont(font)
        self.register_button.setFont(font)
        self.info_status.setFont(font)

        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.username)
        layout.addWidget(self.label2)
        layout.addWidget(self.password)
        layout.addWidget(self.register_button)
        layout.addWidget(self.info_status)

        self.setLayout(layout)
        self.setWindowTitle('Registration')
        self.setGeometry(300, 450, 400, 400)

    def register(self):
        response = requests.get('https://127.0.0.1:5000/reg_info?name=' + self.username.text() + '&)
            

     



def main():
    app = QApplication(sys.argv)
    window = Registration()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
