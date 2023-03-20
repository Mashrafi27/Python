import openpyxl as xl
wb = xl.load_workbook("Python Tutorial Supplementary Materials/transactions.xlsx")
sheet = wb['Sheet1']
print(sheet['a1'].value)

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    print(cell.value)