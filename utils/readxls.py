import xlrd

def gettestdata(x, y):
    testdata = xlrd.open_workbook('./demo/data/dataa.xls')
    table = testdata.sheet_by_name('test_2')
    lvalue = table.cell(x, y).value
    return lvalue


# aa = gettestdata(1, 0)
# print(aa)
