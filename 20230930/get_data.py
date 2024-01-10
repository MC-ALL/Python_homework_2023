import openpyxl, logging

def get_data(path, name_col, weight_col):
    wb = openpyxl.load_workbook(path)
    sheet = wb.worksheets[0]
    detial = {}
    name = []
    weight = []
    name_cell = sheet[name_col]
    weight_cell = sheet[weight_col]
    for i in name_cell:
        name.append(i.value)
    del name[0]
    for i in weight_cell:
        weight.append(i.value)
    del weight[0]
    detial = dict(zip(name, weight))
    logging.debug(detial)
    detial = ({k: v for k, v in detial.items() if v is not None})
    total = sum(detial.values())
    logging.debug(total)

    for i in detial.keys():
        detial[i] = (detial[i], i.split("-")[2])
        logging.debug(detial)
    return detial, total

data = get_data(r"C:\Users\13059\Desktop\测试\销售订单9-28货拉拉06 的副本.xlsx", "J", "L")
print(data)