import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

#Межі інтегрування
a = 0  
b = 2  

#Графік функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

#Монте-Карло 
N = 10000  
x_rand = np.random.uniform(a, b, N)  
y_rand = np.random.uniform(0, max(y), N)  


under_curve = y_rand < f(x_rand)
area_mc = (b - a) * max(y) * np.sum(under_curve) / N

print("Метод Монте-Карло: Обчислена площа =", area_mc)

result, error = spi.quad(f, a, b)
print("Точний інтеграл:", result, "Оцінка помилки:", error)

#Порівняння результатів
print("Різниця між методами:", abs(area_mc - result))
