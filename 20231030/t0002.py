from math import ceil


km = float(input())
km = ceil(km)
print(f"{km} km")

if km <= 3:
    price = 10
elif km <= 10:
    price = (km - 3) * 2 + 10
else:
    price = 7 * 2 + (km - 10) * 3 + 10

print(f"The price is: ${price:.2f}")