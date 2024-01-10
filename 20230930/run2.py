import xlrd

def get_price(file_name):
#    file_name = file_name.encode("utf-8").decode('utf-8')
    work_book = xlrd.open_workbook(file_name)
    table = work_book.sheet()[0]

    cols_values1 = table.col_values(1)
    cols_values2 = table.col_values(2)

    price_list = dict(zip(cols_values1, cols_values2))

    return price_list

price_list = get_price(r"C:\Users\13059\Desktop\测试\价格表.xlsx")
print(price_list)
