def rectangle_area(b, c):
    area = b * c
    return area

b = int(input("Enter the length: "))
c = int(input("Enter the width: "))

print("The area of this rectangle is %d" % (rectangle_area(b, c)))