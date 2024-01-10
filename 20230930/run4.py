import yaml, openpyxl, logging

def load_config(path):
    with open(path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    logging.debug(config)
    return config

def load_price(path):
    with open(path, 'r') as file:
        price = yaml.load(file, Loader=yaml.FullLoader)
    logging.debug(price)
    return price

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



def data_process(price_list, detial, total, real_weight, al_price):
    result = {}
    for i in detial.keys():
        process_fee = price_list[detial[i][1]]
        result[i] = (i, detial[i][0], total, detial[i][0] / total, real_weight, real_weight * detial[i][0] / total, al_price, process_fee, detial[i][1], (al_price + process_fee) * real_weight * detial[i][0] / total / 1000)
    logging.debug(result)
    return result

def save_result(result, path):
    pass

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='./20230930/debug.log')
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')

    price = load_price(r"C:\Users\13059\Desktop\测试\价格表.yaml")
    data = get_data(r"C:\Users\13059\Desktop\测试\销售订单9-28货拉拉06 的副本.xlsx", "J", "L")
    result = data_process(price, data[0], data[1], 777.8, 19870)

    for i in result:
        print(i, result[i])
