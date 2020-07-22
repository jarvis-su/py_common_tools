import pandas as pd

sExcelFile = '../data/复诊名单.xlsx'

base_doctor = pd.read_excel(sExcelFile, sheet_name = 'base_doctor')
doctor7_2_79 = pd.read_excel(sExcelFile, sheet_name = '2020-7-2（79）')
#获取最大行，最大列
nrows=base_doctor.shape[0]
ncols=base_doctor.columns.size


print("=========================================================================")
print('Max Rows: '+str(nrows))
print('Max Columns: '+str(ncols))

for iRow in range(nrows):
    rowContext = ''
    for iCol in range(ncols):
        rowContext = rowContext + ' - ' + str(base_doctor.iloc[iRow,iCol])

    print(rowContext)

for row in range(doctor7_2_79.shape[0]):
    id_number = str(doctor7_2_79.iloc[row][2])
    for iRow in range(nrows):
        cid = str(base_doctor.iloc[iRow,0])
        dept_name = str(base_doctor.iloc[iRow,1])
        doc_name =  str(base_doctor.iloc[iRow,2])
        doc_id_number = str(base_doctor.iloc[iRow,3])
        doc_grade = str(base_doctor.iloc[iRow,4])
        if (doc_id_number.strip() == id_number.strip()):
            print('Find id_number : ' + id_number)
    #print(doc_id_number)
