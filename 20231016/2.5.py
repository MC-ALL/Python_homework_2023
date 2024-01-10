def odd(input):
    if input % 2 == 1:
        return True
    
input = int(input())
if odd(input):
    print("odd")
else:
    print("even")