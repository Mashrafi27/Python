import openpyxl as xl
wb = xl.load_workbook("Python Tutorial Supplementary Materials/transactions.xlsx")
sheet = wb['Sheet1']
print(sheet['a1'].value)