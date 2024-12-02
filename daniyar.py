import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import Qt


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(450, 300, 400, 300)

        self.label = QLabel("Are you gay?", self)
        self.button1 = QPushButton('yes', self)
        




        self.label.move(150, 150)

        self.show()

    def no_button(self):
        self.button2 = QPushButton('no', self)
        self.

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()