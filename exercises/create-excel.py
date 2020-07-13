import openpyxl
import os

os.chdir('/Users/lucasmonteiroi/git-repo/python-course/output-files')
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'].value = 'Hello'
sheet['A2'].value = 'How are you?'
wb.save('example.xlsx')