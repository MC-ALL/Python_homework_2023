import yaml

def load_price(path):
    with open(path, 'r') as yamlfile:
        price = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return price

def load_config(path):
    with open(path, 'r') as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return config

price = load_price(r"C:\Users\13059\Desktop\测试\价格表.yaml")
print(price)