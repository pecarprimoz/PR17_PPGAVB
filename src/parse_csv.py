from openpyxl import load_workbook
'''
    README IF USING
    wb je trenutni workbook, iz katerega beremo
    txtPathWrite je kamor kreiramo nov 

'''
wb = load_workbook("../podatkixlsx/Izbirci.xlsx")
txtPathWrite="../customdata/izbirci_test_testing.txt"
w=open(txtPathWrite, 'w')
workSheet=wb['Izbirci']
dataArray=[]
for line in range(2,5):
    print(line)


w.close()