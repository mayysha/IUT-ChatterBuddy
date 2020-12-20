import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import Create_Account_GUI
import Chat_Window
from PyQt5.QtWidgets import QLabel


class LogInWindow(QtWidgets.QWidget):

    def __init__(self):
        super(LogInWindow, self).__init__()

        self.setFixedSize(900, 700)

        self.top = 400
        self.left = 400
        self.width = 700
        self.height = 400
        self.username = QtWidgets.QLineEdit('Username')
        self.password = QtWidgets.QLineEdit('Password')

        self.login = QtWidgets.QPushButton('LOG IN', self)

        self.no_account = QtWidgets.QLabel('Don\'t have an account?')
        self.signup = QtWidgets.QPushButton('SIGN UP')

        self.login.setIcon(QtGui.QIcon("icons8-password-48.png"))
        self.login.move(300, 800)
        self.login.resize(100, 100)

        self.signup.setIcon(QtGui.QIcon("icons8-signin-48.png"))

        self.init_ui()

    def init_ui(self):

        self.setWindowIcon(QtGui.QIcon("download.png"))

        self.image = QLabel(self)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = QPixmap("robot-2192617_1280.png")
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)

        self.image.setPixmap(pixmap)

        self.username.setStyleSheet(
            "QLineEdit { padding : 25px; font: 25px; border-radius : 10px;}"
        )
        self.password.setStyleSheet(
            "QLineEdit { padding : 25px; font: 25px; border-radius : 10px}"
        )

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.setStyleSheet(
            "QPushButton { background : #2c89a0; padding : 12px; border-radius : 10px; font : 15px }"
        )
        self.signup.setStyleSheet(
            "QPushButton { background : #2c89a0; padding : 12px; border-radius : 10px; font : 15px }"
        )

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.image)

        v_box.addWidget(self.username, 50, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.password, 50, QtCore.Qt.AlignCenter)

        v_box.addWidget(self.login, 0, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.no_account, 0, QtCore.Qt.AlignCenter)
        v_box.addWidget(self.signup, 0, QtCore.Qt.AlignCenter)

        self.login.clicked.connect(self.searching)
        self.signup.clicked.connect(self.goto)

        self.setLayout(v_box)
        self.setWindowTitle('Login')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def searching(self):
        conn = sqlite3.connect('info.db')
        c = conn.cursor()

        dict = {}

        c.execute("SELECT USERNAME, PASSWORD FROM INFORMATION")
        usernames = c.fetchall()

        print(usernames)
        for i in range(len(usernames)):
            usernames[i] = usernames[i][0]

        c.execute("SELECT PASSWORD FROM INFORMATION")
        passwords = c.fetchall()

        print(passwords)
        for i in range(len(passwords)):
            passwords[i] = passwords[i][0]

        for i in range(len(usernames)):
            dict.update({usernames[i]: passwords[i]})

        given_username = self.username.text()
        given_password = self.password.text()


        print(dict)

        if given_username in usernames:
            if given_password == dict[given_username]:
                self.goto_chat_window()
            else:
                print("Password didn't match")
        else:
            print("User doesn't exist")

    def goto(self):
        self.close()
        self.Create_Account = Create_Account_GUI.SignInWindow()
        self.Create_Account.show()

    def goto_chat_window(self):
        self.Chat_Window = Chat_Window.Chat_Window(self.username.text())
        self.close()
        self.Chat_Window.show()
