import json


def parse_page(json_res):


    diseaseData = json.loads(json_res)
    # print(diseaseData)

    contentLen=len(diseaseData['content'])
    contentIndex = 0
    for contentIndex in range(contentLen):
        parentFaculty = diseaseData['content'][contentIndex]['parentFaculty']
        if diseaseData['content'][contentIndex]['secondFaculty'] is None:
            continue
        secondFacultyLen = len(diseaseData['content'][contentIndex]['secondFaculty'])
        secondFacultyIndex = 0
        for secondFacultyIndex in range(secondFacultyLen):
            secondFacultyCategory =  diseaseData['content'][contentIndex]['secondFaculty'][secondFacultyIndex]['secondFacultyCategory']
            diseaseInfoLen = len(diseaseData['content'][contentIndex]['secondFaculty'][secondFacultyIndex]['diseaseInfo'])
            diseaseInfoIndex = 0
            for diseaseInfoIndex in range(diseaseInfoLen):
                diseaseName = diseaseData['content'][contentIndex]['secondFaculty'][secondFacultyIndex]['diseaseInfo'][diseaseInfoIndex]['diseaseName']
                diseaseKey =  diseaseData['content'][contentIndex]['secondFaculty'][secondFacultyIndex]['diseaseInfo'][diseaseInfoIndex]['diseaseKey']
                diseaseId = diseaseData['content'][contentIndex]['secondFaculty'][secondFacultyIndex]['diseaseInfo'][diseaseInfoIndex]['diseaseId']
                print(parentFaculty + ', '+ secondFacultyCategory + ', ' + diseaseName + ',' + diseaseKey + ',' + diseaseId)


def main():
    f = open('../data/diseaseInfo.json', encoding='GBK')
    res = f.read()  # 读文件
    parse_page(res)


if __name__ == '__main__':
    main()

