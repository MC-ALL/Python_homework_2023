import sympy

# def Sin_Taylor_expand(x):
#     expr = sympy.sin(x)
#     n = 5
#     return sympy.series(expr, x, n)

# x = float(input("Enter the value of x: "))
# print("The Taylor series expansion of sin(x) is: ")
# print(Sin_Taylor_expand(x))

# def N_diff(expr, x, n):
#     if n == 0:
#         return expr
#     else:
#         return sympy.diff(expr, x, n)
    

# def Sin_Taylor_expand(x):
#     x = sympy.Symbol("x")
#     expr = sympy.sin(x)
#     n = 5
#     for i in range(1, n):
#         expr = expr + sympy.div(N_diff(expr, 0, i), sympy.factorial(i)) * x
#     return expr

# x = float(input("Enter the value of x: "))
# print("The Taylor series expansion of sin(x) is: ")
# print(Sin_Taylor_expand(x))

# def Sin_Taylor_expand(x0):
#     x = sympy.Symbol("x")
#     expr = sympy.sin(x)
#     n = 5
#     sum = 0
#     for i in range(n):
#         numerator = sympy.diff(expr, x, i)
#         numerator = numerator.evalf(subs={x: 0})
#         denominator = sympy.factorial(i)
#         sum = sum + numerator / denominator * x0 ** i # type: ignore
#     return sum

# print(Sin_Taylor_expand(0.1))

# x = sympy.Symbol("x")
# expr = sympy.sin(x)
# f_expr = sympy.series(expr, x, n = 5).removeO()
# print(f_expr.evalf(subs={x: 0.1}))

def Sin_Taylor_expand():
    x = sympy.Symbol("x")
    expr = sympy.sin(x)
    n = 5
    for i in range(n):
        numerator = sympy.diff(expr, x, i).removeO()
        numerator = numerator.evalf(subs={x: 0})
        denominator = sympy.factorial(i)
        expr += sympy.sympify(numerator / denominator) * x
    return expr

expr = Sin_Taylor_expand()
print(expr)