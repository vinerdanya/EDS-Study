from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt

degrees_of_freedom = [1, 2, 5, 10]

x = np.linspace(0, 20, 1000)

plt.figure(figsize=(8, 5))

for m in degrees_of_freedom:
    plt.plot(x, chi2.pdf(x, m), label=fr'$m={m}$')

plt.xlabel('$x$')
plt.ylabel('$f_W(x)$')
plt.ylim(0, 1)
plt.title('Функция плотности хи-квадрат распределения')
plt.legend()
plt.grid(True)
plt.show()
