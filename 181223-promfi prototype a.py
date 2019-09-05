import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

#name = input("What is your name: ")
#age = int(input("How old are you: "))
#year = str((2014 - age)+100)
#print(name + " will be 100 years old in the year " + year)

#pinS = int(input("enter project number starting value: "))
#pinE = int(input("enter project number ending value: "))
#pinRg = range(start=pinS, stop=pinE)

#finS = int(input("enter file number starting value"))
#finE = int(input("enter file number ending value"))

#tinS = input("enter task code letter starting value")
#tinE = input("enter task code letter ending value")

#rinS = input("enter relationship code letter starting value")
#rinE = input("enter relationship code letter ending value")

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
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())