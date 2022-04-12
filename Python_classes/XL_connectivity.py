from openpyxl import Workbook
wb = Workbook()
wb
sheet = wb.active
sheet
sheet["A1"] = "Hi"
sheet["B1"] = "Saketh"
wb.save(filename="demo_pych.xlsx")
import os
print(os.getcwd())