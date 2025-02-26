from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt

df_pairs = [(1, 5), (5, 5), (10, 10), (20, 10)]

x = np.linspace(0, 5, 1000)

plt.figure(figsize=(8, 5))

for m, n in df_pairs:
    plt.plot(x, f.pdf(x, m, n), label=fr'$m={m}, n={n}$')

plt.xlabel('$x$')
plt.ylabel('$f_W(x)$')
plt.ylim(0, 3)
plt.title('Функция плотности распределения Фишера')
plt.legend()
plt.grid(True)
plt.show()
