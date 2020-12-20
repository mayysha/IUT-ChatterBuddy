import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        btn = QPushButton("Click Me", self)
        btn.clicked.connect(self.onClick)

    def onClick(self):
        self.close()
        self.SW = SecondWindow()
        self.SW.show()


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        lbl = QLabel('Second Window', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())
