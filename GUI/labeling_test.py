import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Labeling')

    s = 'hello new world'

    li = QtWidgets.QLabel(w)
    b1 = QtWidgets.QPushButton(w)

    li.setText("Hello World")

    w.show()
    sys.exit(app.exec_())

window()