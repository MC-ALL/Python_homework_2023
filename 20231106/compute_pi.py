import math
import matplotlib
import matplotlib.pyplot as plt
from mplfonts.bin.cli import init
from mplfonts import use_font
init()
use_font('Noto Sans CJK SC')#指定中文字体
matplotlib.use("TkAgg")

N = 100
L_tmp = 0.0
E_tmp = 0.0
L_result = 0.0
E_result = 0.0
L_results_list = []
E_results_list = []
L_D_list = []
E_D_list = []

for i in range(N):
    L_tmp += (1 / ((4 * i + 1) * (4 * i + 3)))
    L_result = 8 * L_tmp
    L_results_list.append(L_result)
    E_tmp += (1 / (i + 1) ** 2 )
    E_result = (6 * E_tmp) ** 0.5
    E_results_list.append(E_result)
    L_D_list.append(abs(L_result - math.pi))
    E_D_list.append(abs(E_result - math.pi))

plt.figure(dpi=200)
plt.subplot(2, 1, 1)
plt.title("可视化")
plt.plot(range(N), L_results_list, label="L", color="orange")
plt.plot(range(N), E_results_list, label="E", color="blue")
plt.legend()
plt.axis([0, N, 2.8, 3.3]) # type: ignore
plt.subplot(2, 1, 2)
plt.title("相差值")
plt.plot(range(N), L_D_list, label="L_D", color="orange")
plt.plot(range(N), E_D_list, label="E_D", color="blue")
plt.legend()
plt.suptitle("计算圆周率")
plt.show()
