import math

r = 10.6
area_circle = math.pi * (r ** 2)

a = 1.3
b = 1
area_rectangle = a * b

while area_rectangle < area_circle:
    b += 1
    area_rectangle = a * b

print(b - 1)