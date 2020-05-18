#Extract Columns and Rows of an Excel

import xlrd

workbook=xlrd.open_workbook('filename')

#declare the sheet you want to open
sheet=workbook.sheets()[0]

#declare the column you want to obtain
column=sheet.col_values(1) 

#declare the row you want to obtain
row=sheet.row_values(1)
