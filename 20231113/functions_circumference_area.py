def circle_c(r):
    import math
    c = math.pi * r * 2
    return c

def circle_a(r):
    import math
    a = math.pi * r * r
    return a

r = 1
print("The radius of circle is %d, the C is %d, the A is %d", (r, circle_c(r), circle_a(r)))