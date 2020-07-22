#! -*- coding utf-8 -*-
#! @Time  : 2020-7-22 21:28:52
#! Author : Jarvis Su
#! @File  :Pandas_ReadExcelV1.0.py
#! Python Version 3.7

import pandas as pd

print("hello ")

sExcelFile = '../data/复诊名单.xlsx'

data = pd.read_excel(sExcelFile, sheet_name = 'base_doctor')

#获取最大行，最大列
nrows=data.shape[0]
ncols=data.columns.size


print("=========================================================================")
print('Max Rows: '+str(nrows))
print('Max Columns: '+str(ncols))

print(data.head())

#显示列名，以列表形式显示
print(data.columns)

#显示列名，并显示列名的序号
for iCol in range(ncols):
    print(str(iCol)+':'+data.columns[iCol])

#列出特定行列，单元格的值
print(data.iloc[0,0])
print(data.iloc[0,1])

print("=========================================================================")

#查看某列内容
sColumnName='DocCID'
print(data[sColumnName])

#查看第3列的内容，列的序号从0开始
sColumnName=data.columns[2]
print(data[sColumnName])

#查看某行的内容
iRow=1
for iCol in range(ncols):
    print(data.iloc[iRow,iCol])

#遍历逐行逐列
for iRow in range(nrows):
    for iCol in range(ncols):
        print(data.iloc[iRow,iCol])

print('=====================================End==================================')
