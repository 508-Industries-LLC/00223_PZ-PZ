# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\190422_python tutorial - programming with Mosh\PROMFI 2\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 80, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 60, 55, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(220, 80, 111, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.takeText())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "TextLabel"))

    # import os
    # import openpyxl as xl

    # def somefunkeystuff(self):
    #     # import os
    #     # import openpyxl as xl
    #     # os.chdir('F:/00085-PROGRAMMING & CODING PROJECTS/Python Programming/190422_python tutorial - programming with Mosh/PROMFI 2')
    #     # projects_workbook = xl.load_workbook('Book1.xlsx', data_only=True)
    #     # tasks_sheet = projects_workbook['Sheet2']
    #     # task_code_selection = tasks_sheet.cell(2, 3)
    #     # var1 = "x" #task_code_selection.value
    #     # print(var1)
    #     self.textEdit.setText("x")

    # def task_code():
    #     os.chdir('F:/00223-PROMFI DATABASE SYSTEM MANAGER/3.5.1 - 00223-PZ-PZ PROMFI SYSTEM')
    #     projects_workbook = xl.load_workbook('PROMFI 1.4.xlsx', data_only=True)
    #     tasks_sheet = projects_workbook['TAP.P']
    #     guess1 = input('guess a family task code: ')
    #     guess2 = input('guess a parent task code: ')
    #     print(f"Task Code Options are: ")
    #
    #     for row in range(16, tasks_sheet.max_row + 1):
    #         task_code_selection = tasks_sheet.cell(row, 3)
    #         family_task_code = tasks_sheet.cell(row, 4)
    #         family_task_description = tasks_sheet.cell(row, 5)
    #         parent_task_code = tasks_sheet.cell(row, 6)
    #         parent_task_description = tasks_sheet.cell(row, 7)
    #         child_task_code = tasks_sheet.cell(row, 8)
    #         child_task_description = tasks_sheet.cell(row, 9)
    #         task_options_list = {
    #             task_code_selection.value: family_task_code.value,
    #             task_code_selection.value: family_task_description.value,
    #             task_code_selection.value: parent_task_code.value,
    #             task_code_selection.value: parent_task_description.value,
    #             task_code_selection.value: child_task_code.value,
    #             task_code_selection.value: child_task_description.value
    #         }
    #
    #         if guess1 == family_task_code.value and guess2 == parent_task_code.value:
    #             #  and guess3 == child_task_description.value
    #             print(f"{task_options_list}")  # , end=" "


    def takeText(self):
        gunit = self.textEdit.currentText()
        self.textEdit.setText(gunit)
        # # Project Number Selector
        # aa = self.comboBox_14.currentText() # 67589
        # ab = self.comboBox_15.currentText()
        # ac = self.comboBox_16.currentText()
        # ad = self.comboBox_17.currentText()
        # ae = self.comboBox_18.currentText()
        # af = aa + ab + ac + ad + ae
        # # Resource Number Selector
        # ba = self.comboBox_19.currentText() # 67589
        # bb = self.comboBox_20.currentText()
        # bc = self.comboBox_21.currentText()
        # bd = self.comboBox_22.currentText()
        # be = ba + bb + bc + bd
        # # Task Code Selector
        # ca = self.comboBox_12.currentText()
        # cb = self.comboBox_9.currentText()
        # cc = self.comboBox_13.currentText()
        # cd = self.comboBox_10.currentText()
        # ce = ca + cb + "-" + cc + cd
        # # Relationship Code Selector
        # da = self.comboBox.currentText()
        # db = self.comboBox_2.currentText()
        # dc = self.comboBox_3.currentText()
        # dd = self.comboBox_4.currentText()
        # de = self.comboBox_5.currentText()
        # df = self.comboBox_6.currentText()
        # de = da + db + dc + "." + dd + "." + de + "." + df
        # # sequence combinator
        # combined_sequence = af + "-" + be + "_" + ce + de
        # # combined_sequence_2 = af + "-" + be + "_" + ce + de + "OLEX"
        # self.textEdit.setText(combined_sequence)
        # # self.textEdit.setText(combined_sequence_2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

