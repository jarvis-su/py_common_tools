import pandas as pd

print("hello ")

file = 'C:/Users/JarvisSu/OneDrive/workSpace/Careate/互联网医院/医生医院数据/复诊名单.xlsx'

data = pd.read_excel(file, sheet_name = 'base_doctor')
print(data.head())
