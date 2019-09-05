import xlrd
file_location = "C:\Users\Ziloeh\GD_508\PROMFI\00223-PROMFI DATABASE SYSTEM MANAGER [DASYMA]\PROMFI 1.0.xlsx"
workbook = xlrd.open_workbook('file_locaiton')
sheet = workbook.sheet_by_index(3)
r = sheet.nrows
print("r")
