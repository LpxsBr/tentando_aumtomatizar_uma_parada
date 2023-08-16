from openpyxl import load_workbook

wb = load_workbook(filename='modelo.xlsx')

for i in range(1, 1000):
    if(wb['dados'][f'B0{i+1}'].value == None):
        break
    print(wb['dados'][f'B0{i}'].value)