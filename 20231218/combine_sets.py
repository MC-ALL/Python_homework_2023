def gen_cards():
    ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    cards = []
    for i in suits:
        for j in ranks:
            cards.append(j+i)
    return cards

def gen_number():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    car_number = []
    for i1 in alpha:
        for i2 in alpha:
            for j1 in number:
                for j2 in number:
                    for j3 in number:
                        car_number.append(i1+i2+j1+j2+j3)
    return car_number

def gen_dice():
    result = []
    for i in range(1,7):
        for j in range(1,7):
            if i + j == 7:
                result.append(str(i)+','+str(j))
    return result

if __name__ == '__main__':
    print(gen_cards())
    print(gen_number())
    print(gen_dice())


