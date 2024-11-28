import sys
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from collections import defaultdict
import requests


class Chat:
    def __init__(self):
        self.users = {}
        self.messages = {}

users = []
messages = defaultdict(list)
me = []
result = [False]

class All_messages(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)
        self.setWindowTitle('All messages')
        self.setGeometry(200, 200, 400, 400)
        self.show()



class Registration(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)

        self.label = QLabel("username")
        self.username = QLineEdit()
        self.label2 = QLabel("password")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton("Register")

        font = QFont()
        font.setPointSize(14) 
        
        self.label.setFont(font)
        self.username.setFont(font)
        self.label2.setFont(font)
        self.password.setFont(font)
        self.register_button.setFont(font)

        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.username)
        layout.addWidget(self.label2)
        layout.addWidget(self.password)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
        self.setWindowTitle('Registration')
        self.setGeometry(200, 200, 400, 400)
    
    def register(self):
        username = self.username.text()
        password = self.password.text()
        if password == '12345':
            if len(username) > 0:
                me.append(username)
                result[0] = True
                self.close()
        else:
            msg = QMessageBox(self, f"Wrong Password")
            msg.show()
            result[0] = False

    

class NewUser(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)

        self.label = QLabel("New User Name")
        self.contact = QLineEdit()
        self.add_button = QPushButton("Add new user")

        font = QFont()
        font.setPointSize(14) 
        
        self.label.setFont(font)
        self.contact.setFont(font)
        self.add_button.setFont(font)

        self.add_button.clicked.connect(self.add)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.contact)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('NEW CONTACT')
        self.setGeometry(200, 200, 400, 400)
    
    def add(self):
        user = self.contact.text()
        if len(user) > 0:
            users.append(user)
            self.label.setText(f'Added new user : {user}')
            self.contact.clear()
    

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.register = Registration()
        self.register.exec()

        if result[0] == True:
            self.msg_dict = defaultdict(list)

            self.contacts = QTextEdit()
            self.contacts.setReadOnly(True)
            self.messages = QTextEdit()
            self.add_user_button = QPushButton("Add new user")
            self.show_all_messages = QPushButton("Show all messages")
            self.messages.setReadOnly(True)
            self.message = QLineEdit()
            self.send_button = QPushButton("Send")
            
            font = QFont()
            font.setPointSize(14) 
            
            self.contacts.setFont(font)
            self.message.setFont(font)
            self.messages.setFont(font)
            self.send_button.setFont(font)
            self.add_user_button.setFont(font)
            self.show_all_messages.setFont(font)

            self.send_button.clicked.connect(self.send)
            self.contacts.selectionChanged.connect(self.show_messages)
            self.add_user_button.clicked.connect(self.add_new_user)
            self.show_all_messages.clicked.connect(self.All_messages())


            layout = QVBoxLayout()
            layout.addWidget(self.contacts)
            layout.addWidget(self.add_user_button)
            layout.addWidget(self.messages)
            layout.addWidget(self.message)
            layout.addWidget(self.send_button)

            self.setLayout(layout)
            self.setWindowTitle('AIT CHAT 2024')
            self.setGeometry(200, 200, 600, 800)

    def send(self):
        sender = me[0]
        receiver = self.contacts.textCursor().selectedText()
        message = self.message.text()
        if len(receiver) > 0 and len(message) > 0:
            url = 'https://ait23.pythonanywhere.com/addChat'
            data = {'sender': sender, 'receiver': receiver, 'message': message}
            requests.get(url, json= data)
            self.show_messages()
            self.message.clear()

    def show_messages(self):
        sender = me[0]
        receiver = self.contacts.textCursor().selectedText()
        if len(receiver) > 0:
            url = 'https://ait23.pythonanywhere.com/getChat'
            response = requests.get(url, json= {'sender': sender})
            r = response.json().get('response', '').split('\n')
            arr = []
            for i in r:
                if f'{sender}' in i:
                    arr.append(i)
            self.messages.setText('\n'.join(arr))
    

    
    def add_new_user(self):
        self.new_user = NewUser()
        self.new_user.exec()
        self.contacts.setText('\n'.join(users))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
