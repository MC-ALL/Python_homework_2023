def square_area(N):
    s_area = N * N
    return s_area

def circle_area(N):
    import math
    c_area = math.pi * N * N
    return c_area

N = int(input("Enter a number: "))
print(square_area(N), circle_area(N), square_area(N) / circle_area(N))
