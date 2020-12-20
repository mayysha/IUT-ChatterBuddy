import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel

import Chat_Window
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5 import QtCore

conn = sqlite3.connect('info.db')
c = conn.cursor()


class SignInWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SignInWindow, self).__init__()

        self.setFixedSize(900, 700)

        self.email = QtWidgets.QLineEdit('Email Address')
        self.username = QtWidgets.QLineEdit('Username')
        self.password = QtWidgets.QLineEdit('Password')
        self.signup = QtWidgets.QPushButton('Sign Up')

        self.init_ui()

    def init_ui(self):
        self.image = QLabel(self)
        self.image.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = QPixmap("robot-2192617_1280.png")
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)

        self.email.setStyleSheet(
            "QLineEdit { padding : 25px; font: 25px; border-radius : 10px;}"
        )
        self.username.setStyleSheet(
            "QLineEdit { padding : 25px; font: 25px; border-radius : 10px;}"
        )
        self.password.setStyleSheet(
            "QLineEdit { padding : 25px; font: 25px; border-radius : 10px;}"
        )

        self.signup.setStyleSheet(
            "QPushButton { background : #2c89a0; padding : 12px; border-radius : 10px; font : 15px }"
        )

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.image)
        v_box.addWidget(self.email, 50, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.username, 50, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.password, 50, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.signup, 0, QtCore.Qt.AlignCenter)

        self.signup.clicked.connect(self.add_row)

        self.setLayout(v_box)

        self.setWindowIcon(QtGui.QIcon("download.png"))

        self.setWindowTitle('SignUp')

        self.show()

    def add_row(self):
        row = [self.email.text(), self.username.text(), self.password.text()]

        print(row)

        strr = "INSERT INTO INFORMATION VALUES('{}', '{}', '{}');".format(row[0], row[1], row[2])

        print(strr)

        c.execute(strr)

        conn.commit()

        self.goto_chat_window()

    def goto_chat_window(self):
        self.Chat_Window = Chat_Window.Chat_Window(self.username.text())
        self.close()
        self.Chat_Window.show()
