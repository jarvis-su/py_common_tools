import pandas as pd
from datetime import datetime
import time

sExcelFile = 'C:/Users/sujie.Careate/Desktop/2020-8-8查询.xlsx'

intg_status_detail = pd.read_excel(sExcelFile, sheet_name='Sheet1')

# 获取最大行，最大列
nrows = intg_status_detail.shape[0]
ncols = intg_status_detail.columns.size

print("=========================================================================")
print('Max Rows: ' + str(nrows))
print('Max Columns: ' + str(ncols))
next_row = 0
total_duration = 0
for row in range(nrows - 1):
    next_row = row + 1

    # DetailID = str(intg_status_detail.iloc[row, 0])

    IGSaleID = str(intg_status_detail.iloc[row, 1])
    next_igsaleID = str(intg_status_detail.iloc[next_row, 1])

    BussStatus = intg_status_detail.iloc[row, 2]
    next_BussStatus = intg_status_detail.iloc[next_row, 2]

    DeptID = str(intg_status_detail.iloc[row, 11])
    DeptName = str(intg_status_detail.iloc[row, 12])
    DocID = str(intg_status_detail.iloc[row, 13])
    DoctorName = str(intg_status_detail.iloc[row, 14])
    DoctorLevel = str(intg_status_detail.iloc[row, 15])
    Meaning = str(intg_status_detail.iloc[row, 16])

    if BussStatus == 11 and next_BussStatus == 3 and next_igsaleID == IGSaleID:
        # print('接诊了')
        AddTime = intg_status_detail.iloc[row, 8]
        end_time = intg_status_detail.iloc[next_row, 8]
        duration = end_time - AddTime
        # print(duration)

        total_duration = total_duration + duration.days * 24 * 60 * 60 + duration.seconds
        # print('IGSaleID' + IGSaleID + ', AddTime = ' + str(AddTime) + ' , end_time = ' + str(end_time))
    if next_igsaleID != IGSaleID or next_row == nrows-1:
        # print('IGSaleID total duration is : ' + str(total_duration))
        print(
            IGSaleID + ',' + DeptName + ',' + DocID + ',' + DoctorName + ',' + DoctorLevel + ',' + Meaning + ',' + str(
                total_duration))
        total_duration = 0

    # BussTime = str(intg_status_detail.iloc[row, 3])
    # BussReason = str(intg_status_detail.iloc[row, 4])
    # Source = str(intg_status_detail.iloc[row, 5])
    # IsDel = str(intg_status_detail.iloc[row, 6])
    # IsEnabled = str(intg_status_detail.iloc[row, 7])
    # AddTime = str(intg_status_detail.iloc[row, 8])
    # OperName = str(intg_status_detail.iloc[row, 9])
    # OperTime = str(intg_status_detail.iloc[row, 10])

    # print(DetailID + ','+ IGSaleID + ',' + BussStatus + ',' + AddTime)
    # print(doc_id_number)
