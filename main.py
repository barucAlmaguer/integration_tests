import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as itgrt

#funciones a evaluar:
def f1(x):
    return x**2

def if1(st, fn):
    #return (fn-st)**3/3
    return (fn**3)/3 - (st**3)/3

def f2(x):
    return x

def f3(x):
    return np.exp(x)
#generacion de lista de datos en base a funcion
steps = 10
st = 0
fn = 20
x2 = np.linspace(st, fn, steps)
#y2 = [(xi-(max(x2) - min(x2))/2)**2 + 50 for xi in x2]
y2 = [f1(xi) for xi in x2]
#x = list(range(0, 20))
#y = [(xi-10)**2 + 50 for xi in x]
print("int simbolica = {}".format(if1(x2[0], x2[-1]) / (max(x2) - min(x2))))

#obtención de integral por diferentes métodos de integración numérica
#promedio
prom = np.mean(y2)
prom_list = [prom for i in range(0, steps)]
print("promedio = {}".format(prom))
#integral de simpson
simpson = itgrt.simps(y2, x2) / (max(x2) - min(x2))
sim_list = [simpson for i in range(0, steps)]
print("simpson = {}".format(simpson))

plt.plot(x2, y2)
plt.plot(x2, prom_list)
plt.plot(x2, sim_list)
plt.show()