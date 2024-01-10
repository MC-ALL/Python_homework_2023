import sympy
from matplotlib import pyplot as plt
import numpy as np

# def Sin_Taylor_expand(n):
#     x = sympy.Symbol('x')
#     expr = sympy.sin(x)
#     expr_result = expr.subs(x, 0)
#     for i in range(n):
#         numerator = sympy.diff(expr, x, i)
#         numerator = numerator.subs(x, 0)
#         denominator = sympy.factorial(i)
#         expr_result += sympy.sympify(numerator / denominator) * x ** i # type: ignore
#     return expr_result

# expr = Sin_Taylor_expand(5)
# print(expr)
# print(expr.evalf(subs={'x': 0.1})) # type: ignore

# x = sympy.Symbol('x')
# print(sympy.series(sympy.sin(x), x, 0, 5).removeO().subs({'x': 0.1}))

def Taylor_expand(expr, x, x0, n):
    expr = expr.subs(x, x0)
    expr_result = sympy.sympify(0)
    for i in range(n):        
        numerator = sympy.diff(expr, x0, i)
        denominator = sympy.factorial(i)
        expr_result += sympy.sympify(numerator / denominator) * (x - x0) ** i # type: ignore
    return expr_result

x = sympy.symbols('x')
x0 = sympy.symbols('x0')
expr = sympy.sin(x)

# print(Taylor_expand(expr, x, x0, 5))
# print(sympy.series(sympy.sin(x), x, x0, 5).removeO())

sin_f = sympy.lambdify([x, x0], Taylor_expand(expr, x, x0, 5))
x_f = sympy.lambdify([x], expr)
x_list = np.linspace(-1 * np.pi, 1 * np.pi, 100)

plt.plot(x_list, [sin_f(x, 0) for x in x_list], label="Taylor_expand")
plt.plot(x_list, [x_f(x) for x in x_list], label="sin(x)")
plt.legend()
plt.show()