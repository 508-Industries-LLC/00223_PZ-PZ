# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\00085-PROGRAMMING & CODING PROJECTS\Python Programming\190422_python tutorial - programming with Mosh\PROMFI 2\TAP.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from TaskCodeSequenceGenerator import TaskCodeSequenceGeneratorMain as tc_main



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow

# class MyTable(QTableWidget):
#     def __init__(self, r, c):
#         super.__init__(r, c)
#
#         self.show()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 176)
        self.ok_cancel_buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.ok_cancel_buttonBox.setGeometry(QtCore.QRect(50, 130, 341, 32))
        self.ok_cancel_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel_buttonBox.setObjectName("ok_cancel_buttonBox")
        # self.tasks_list_comboBox = QtWidgets.QComboBox(Dialog)
        # self.tasks_list_comboBox.setGeometry(QtCore.QRect(20, 30, 381, 22))
        # font = QtGui.QFont()
        # font.setFamily("Nasalization")
        # self.tasks_list_comboBox.setFont(font)
        # self.tasks_list_comboBox.setEditable(True)
        # self.tasks_list_comboBox.setDuplicatesEnabled(True)
        # self.tasks_list_comboBox.setObjectName("tasks_list_comboBox")
        # self.tasks_list_label = QtWidgets.QLabel(Dialog)
        # self.tasks_list_label.setGeometry(QtCore.QRect(30, 10, 81, 16))
        # font = QtGui.QFont()
        # font.setFamily("Nasalization")
        # self.tasks_list_label.setFont(font)
        # self.tasks_list_label.setAcceptDrops(False)
        # self.tasks_list_label.setWordWrap(True)
        # self.tasks_list_label.setObjectName("tasks_list_label")
        # self.task_codes_label = QtWidgets.QLabel(Dialog)
        # self.task_codes_label.setGeometry(QtCore.QRect(30, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        # self.task_codes_label.setFont(font)
        # self.task_codes_label.setObjectName("task_codes_label")
        # tg_func = tc_main.task_code(self.setupUi(Dialog))
        self.task_codes_comboBox = QtWidgets.QComboBox(Dialog)
        self.task_codes_comboBox.setGeometry(QtCore.QRect(20, 90, 131, 22))
        tg_func = tc_main.task_code(self.task_codes_comboBox)
        # font = QtGui.QFont()
        # font.setFamily("Nasalization")
        # self.task_codes_comboBox.setFont(font)
        # self.task_codes_comboBox.setEditable(True)
        # self.task_codes_comboBox.setDuplicatesEnabled(True)
        # self.task_codes_comboBox.setObjectName("task_codes_comboBox")

        self.retranslateUi(Dialog)
        self.ok_cancel_buttonBox.accepted.connect(Dialog.accept)
        self.ok_cancel_buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # self.tasks_list_comboBox.clicked.connect(self.task_code)
        self.task_codes_comboBox.insertItem(tg_func)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.tasks_list_label.setText(_translate("Dialog", "Tasks List"))
        # self.task_codes_label.setText(_translate("Dialog", "Task Codes"))


# import os
# import openpyxl as xl
#
#
# def task_code(self):
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
#             # print(f"{task_options_list}") # , end=" "
#             self.textEdit.setText(task_options_list)


# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference


# def wkbk(self):
#     wb = xl.load_workbook('Book1.xlsx')
#     sht = wb['Sheet1']
#     val: sht['a1']
#     self.textEdit.setText(val)
    # clz = sht['a2']
    # clz = sht.cell(1,1)
    # print(sht.max_row)
    # print(clz.value)

    # for x in range(2, sht.max_row+ 1):
    #     clz = sht.cell.value
    #     # for y in range(1, sht.max_row +1):
    #     #     clz = Reference(sht, max_col=y, max_row=x)
    #     #     print(clz.value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

