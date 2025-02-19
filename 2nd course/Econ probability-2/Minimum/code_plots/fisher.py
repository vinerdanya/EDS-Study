from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt

df_pairs = [(1, 5), (5, 5), (10, 10), (20, 10)]

x = np.linspace(0, 5, 1000)

plt.figure(figsize=(8, 5))

for k, m in df_pairs:
    plt.plot(x, f.pdf(x, k, m), label=fr'$k={k}, m={m}$')

plt.xlabel('$x$')
plt.ylabel('$f_F(x)$')
plt.ylim(0, 3)
plt.title('Функция плотности распределения Фишера')
plt.legend()
plt.grid(True)
plt.show()
