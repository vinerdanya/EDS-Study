from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df_values = [1, 3, 5, 10]

x = np.linspace(-5, 5, 1000)

plt.figure(figsize=(8, 5))

for df in df_values:
    plt.plot(x, t.pdf(x, df), label=fr'$k={df}$')

plt.plot(x, norm.pdf(x, 0, 1), 'k--', label=r'$\mathcal{N}(0,1)$')

plt.xlabel('$x$')
plt.ylabel('$f_T(x)$')
plt.title('Функция плотности распределения Стьюдента')
plt.legend()
plt.grid(True)
plt.show()
