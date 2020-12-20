import sys
from PyQt5 import QtWidgets
import Log_In_Window

app = QtWidgets.QApplication(sys.argv)
w = Log_In_Window.LogInWindow()
sys.exit(app.exec_())