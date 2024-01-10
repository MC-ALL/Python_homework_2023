import sympy
import math

x = sympy.Symbol("x")

f = sympy.atan(x) / ( x ** 2 + 1) # type: ignore

df = sympy.diff(f, x)

dfx = sympy.lambdify(x, df, "math")

#print(dfx(math.pi / 6))
#print(sympy.diff(f, x).subs(x, math.pi / 6))

sympy.plot((df, (x, -math.pi, math.pi)),(f, (x, -math.pi, math.pi)))