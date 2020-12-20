import sqlite3
import intents
import Log_In_Window
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui

conn = sqlite3.connect('info.db')
c = conn.cursor()


class Chat_Window(QtWidgets.QWidget):
    def __init__(self, username):
        super(Chat_Window, self).__init__()

        self.setFixedSize(900, 700)

        self.username = username
        self.prev = 0
        self.flag = 0
        self.buffer_msg = ''

        self.msg1 = QtWidgets.QLabel()
        self.msg2 = QtWidgets.QLabel()
        self.msg3 = QtWidgets.QLabel()
        self.msg4 = QtWidgets.QLabel()
        self.msg5 = QtWidgets.QLabel()
        self.msg6 = QtWidgets.QLabel()
        self.msg7 = QtWidgets.QLabel()
        self.msg8 = QtWidgets.QLabel()
        self.msg9 = QtWidgets.QLabel()
        self.msg10 = QtWidgets.QLabel()

        self.machinelabel = QtWidgets.QLabel()

        self.msg2.setAlignment(QtCore.Qt.AlignRight)
        self.msg4.setAlignment(QtCore.Qt.AlignRight)
        self.msg6.setAlignment(QtCore.Qt.AlignRight)
        self.msg8.setAlignment(QtCore.Qt.AlignRight)
        self.msg10.setAlignment(QtCore.Qt.AlignRight)

        self.labels = [
            self.msg1,
            self.msg2,
            self.msg3,
            self.msg4,
            self.msg5,
            self.msg6,
            self.msg7,
            self.msg8,
            self.msg9,
            self.msg10
        ]

        for i in range(10):
            self.labels[i].setText('')
            self.labels[i].setWordWrap(True)

        self.previous_messages = QtWidgets.QPushButton("Previous Messages")
        self.previous_messages.setIcon(QtGui.QIcon('back-arrow.png'))
        self.write_message = QtWidgets.QLineEdit()
        self.newer_messages = QtWidgets.QPushButton("Newer Messages")
        self.newer_messages.setIcon(QtGui.QIcon('new-email-envelope.png'))
        self.send_button = QtWidgets.QPushButton('Send')
        self.send_button.setIcon(QtGui.QIcon('send (5).png'))
        self.delete_button = QtWidgets.QPushButton('Delete Conversation')
        self.delete_button.setIcon(QtGui.QIcon('rubbish-bin.png'))
        self.logout_button = QtWidgets.QPushButton('Logout')
        self.logout_button.setIcon(QtGui.QIcon('logout.png'))

        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QtGui.QIcon("download.png"))
        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.previous_messages)

        v_box.addWidget(self.msg1)
        v_box.addWidget(self.msg2)
        v_box.addWidget(self.msg3)
        v_box.addWidget(self.msg4)
        v_box.addWidget(self.msg5)
        v_box.addWidget(self.msg6)
        v_box.addWidget(self.msg7)
        v_box.addWidget(self.msg8)
        v_box.addWidget(self.msg9)
        v_box.addWidget(self.msg10)

        v_box.addWidget(self.machinelabel)

        v_box.addWidget(self.newer_messages)
        v_box.addWidget(self.write_message)
        v_box.addWidget(self.send_button)
        v_box.addWidget(self.delete_button)
        v_box.addWidget(self.logout_button)


        self.previous_messages.clicked.connect(self.get_previous_messages)

        self.newer_messages.clicked.connect(self.get_newer_messages)

        self.send_button.clicked.connect(self.add_message)

        self.send_button.setAutoDefault(True)

        self.write_message.returnPressed.connect(self.send_button.click)

        self.delete_button.clicked.connect(self.delete_all)

        self.logout_button.clicked.connect(self.logout)

        self.setLayout(v_box)

        self.setWindowTitle('Chat')

        self.show()

        self.get_messages()

    def add_message(self):
        line = "INSERT INTO MESSAGES VALUES('{}', '{}', \"{}\");".format('bot', self.username,
                                                                         self.write_message.text())
        line2 = "INSERT INTO MESSAGES VALUES('{}', '{}', \"{}\");".format(self.username, 'bot',
                                                                            intents.bot_answer(self.write_message.text()))

        if self.flag == 1:
            line3 = "INSERT INTO LEARNING VALUES(\"{}\", \"{}\");".format(self.buffer_msg,
                                                                             self.write_message.text())
            c.execute(line3)

            print(self.buffer_msg)

            self.buffer_msg = ''
            print("DONE")

        c.execute(line)
        c.execute(line2)

        self.write_message.setText('')

        conn.commit()

        

        self.get_messages()

    def get_messages(self):
        line_lis = []

        line = """
            SELECT FROM_USER, MESSAGE
            FROM MESSAGES
            WHERE FROM_USER = '{}'
            OR TO_USER = '{}';
        """.format(self.username, self.username)

        c.execute(line)

        extracted_messages = c.fetchall()

        for i in range(len(extracted_messages)):
            username = extracted_messages[i][0]
            message = extracted_messages[i][1]

            display_message = username + ": " + message

            line_lis.append(display_message)

        text1 = ''
        text2 = ''
        text3 = ''
        text4 = ''
        text5 = ''
        text6 = ''
        text7 = ''
        text8 = ''
        text9 = ''
        text10 = ''

        texts = [
            text1,
            text2,
            text3,
            text4,
            text5,
            text6,
            text7,
            text8,
            text9,
            text10
        ]

        j = 0
        for i in range(len(line_lis)):
            texts[j] = line_lis[len(line_lis) - 1 - i]
            j += 1
            if j == 10:
                break

        print(texts)

        if texts[1] == texts[3] and texts[1] != '':
            print(".")
            self.machinelabel.setText("I see you have asked the question twice in a row. Plz tell me, how to answer it. I am still learning")
            self.machinelabel.show()
            self.buffer_msg = texts[1][10:]
            self.flag = 1
        else:
            self.machinelabel.close()
            self.flag = 0


        for i in range(10):
            self.labels[len(self.labels) - 1 - i].setText(texts[i])
            if texts[i] != '' and i % 2 == 0:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #0099ff; border-radius: 10px; color : white; font: 15px; margin-right : 300px }")
            elif texts[i] != '' and i % 2 == 1:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #c3c5c9; border-radius: 10px; color : black; font: 15px; margin-left : 300px }")

    def delete_all(self):
        line = """
                DELETE
                FROM MESSAGES
                WHERE TO_USER = '{}'
                OR FROM_USER = '{}';
            """.format(self.username, self.username)

        c.execute(line)

        for i in range(10):
            self.labels[i].setText('')

    def get_previous_messages(self):
        line_lis = []

        line = """
            SELECT FROM_USER, MESSAGE
            FROM MESSAGES
            WHERE FROM_USER = '{}'
            OR TO_USER = '{}';
        """.format(self.username, self.username)

        c.execute(line)

        extracted_messages = c.fetchall()

        for i in range(len(extracted_messages)):
            username = extracted_messages[i][0]
            message = extracted_messages[i][1]

            display_message = username + ": " + message

            line_lis.append(display_message)

        text1 = ''
        text2 = ''
        text3 = ''
        text4 = ''
        text5 = ''
        text6 = ''
        text7 = ''
        text8 = ''
        text9 = ''
        text10 = ''

        texts = [
            text1,
            text2,
            text3,
            text4,
            text5,
            text6,
            text7,
            text8,
            text9,
            text10
        ]

        j = 0
        self.prev += 10
        for i in range(self.prev, len(line_lis)):
            texts[j] = line_lis[len(line_lis) - 1 - i]
            j += 1
            if j == 10:
                break

        print(texts)

        for i in range(10):
            self.labels[len(self.labels) - 1 - i].setText(texts[i])
            if texts[i] != '' and i % 2 == 0:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #0099ff; border-radius: 10px; color : white; font: 15px; margin-right : 300px }")
            elif texts[i] != '' and i % 2 == 1:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #c3c5c9; border-radius: 10px; color : black; font: 15px; margin-left : 300px }")
            else:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #f0f0f0; border-radius: 10px; color : #f0f0f0; font: 15px; margin-left : 300px }")

    def get_newer_messages(self):
        line_lis = []

        line = """
            SELECT FROM_USER, MESSAGE
            FROM MESSAGES
            WHERE FROM_USER = '{}'
            OR TO_USER = '{}';
        """.format(self.username, self.username)

        c.execute(line)

        extracted_messages = c.fetchall()

        for i in range(len(extracted_messages)):
            username = extracted_messages[i][0]
            message = extracted_messages[i][1]

            display_message = username + ": " + message

            line_lis.append(display_message)

        text1 = ''
        text2 = ''
        text3 = ''
        text4 = ''
        text5 = ''
        text6 = ''
        text7 = ''
        text8 = ''
        text9 = ''
        text10 = ''

        texts = [
            text1,
            text2,
            text3,
            text4,
            text5,
            text6,
            text7,
            text8,
            text9,
            text10
        ]

        j = 0
        self.prev -= 10
        for i in range(self.prev, len(line_lis)):
            texts[j] = line_lis[len(line_lis) - 1 - i]
            j += 1
            if j == 10:
                break

        print(texts)
        for i in range(10):
            self.labels[len(self.labels) - 1 - i].setText(texts[i])
            if texts[i] != '' and i % 2 == 0:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #0099ff; border-radius: 10px; color : white; font: 15px; margin-right : 300px }")
            elif texts[i] != '' and i % 2 == 1:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #c3c5c9; border-radius: 10px; color : black; font: 15px; margin-left : 300px }")
            else:
                self.labels[len(self.labels) - 1 - i].setStyleSheet(
                    "QLabel { padding: 7px; background: #f0f0f0; border-radius: 10px; color : #f0f0f0; font: 15px; margin-left : 300px }")

    def logout(self):
        self.close()
        self.Log_In_Window = Log_In_Window.LogInWindow()
        self.Log_In_Window.show()
