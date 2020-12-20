#incomplete
import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        l1 = QtWidgets.QLabel()
        l2 = QtWidgets.QLabel()
        l3 = QtWidgets.QLabel()
        b_signup = QtWidgets.QPushButton()

        l1.setText('Welcome to IUT ChatterBuddy.'
                   'How can I help you?')
        l2.setPixmap(QtGui.QPixmap('images.png'))
        b_signup.setText('Sign up!')
        l3.setText('Login here....')

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(l1)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(l2)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(l3)
        h_box3.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.le)
        v_box.addWidget(b_signup)


        self.setLayout(v_box)

        self.setWindowTitle('Front Page')

        self.show()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
