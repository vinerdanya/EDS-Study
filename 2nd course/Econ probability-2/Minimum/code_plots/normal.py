import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

params = [
    (0, 1),
    (0, 2),
    (-2, 1),
    (2, 0.5)
]

x = np.linspace(-5, 5, 1000)

plt.figure(figsize=(8, 5))

for mu, sigma in params:
    plt.plot(x, norm.pdf(x, mu, sigma), label=fr'$\mu={mu}, \sigma={sigma}$')

plt.xlabel('$x$')
plt.ylabel('$f_X(x)$')
plt.title('Функция плотности нормального распределения')
plt.legend()
plt.grid(True)
plt.show()