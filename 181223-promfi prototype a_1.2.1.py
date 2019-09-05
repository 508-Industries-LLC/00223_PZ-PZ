import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget, QMessageBox

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        pbtn = QPushButton('Project#', self)
        #pbtn.clicked.connect(QApplication.instance().quit)
        pbtn.clicked.connect(QApplication.instance().quit)
        pbtn.resize(pbtn.sizeHint())
        pbtn.move(10, 10)

        fbtn = QPushButton('File#', self)
        fbtn.clicked.connect(QApplication.instance().quit)
        #fbtn.clicked.connect(QApplication.instance().beep)
        fbtn.resize(fbtn.sizeHint())
        fbtn.move(10, 40)

        tbtn = QPushButton('Task Code', self)
        tbtn.clicked.connect(QApplication.instance().quit)
        #tbtn.clicked.connect(QApplication.instance().beep)
        tbtn.resize(tbtn.sizeHint())
        tbtn.move(10, 70)

        rbtn = QPushButton('Relationship Code', self)
        rbtn.clicked.connect(QApplication.instance().quit)
        #rbtn.clicked.connect(QApplication.instance().beep)
        rbtn.resize(rbtn.sizeHint())
        rbtn.move(10, 100)

        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('PROMFI 2.0 prototype a')

    def __init__(self):
        super().__init__()

        self.initUI()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')

    def __init__(self):
        super().__init__()

        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())