def factorial(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

result = 0

for i in range(1,11):
    result += factorial(i)


print(result)

