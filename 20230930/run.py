import xlwings as xw

def get_data(file_path):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    price_data = app.books.open(file_path)
    sheet = price_data.sheets[0]

    each_price = {}
    item = sheet.range["A1"].value
    value = sheet.range["B1"].value
    each_price = dict(zip(item, value))

    price_data.close()
    app.quit()
    return each_price

each_price = get_data(r"C:\Users\13059\Desktop\测试\价格表.xlsx")
print(each_price)

