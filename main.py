import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as itgrt

#funciones a evaluar:
#y = x**2
def f1(x):
    return x**2
def if1(st, fn):
    #return (fn-st)**3/3
    return (fn**3)/3 - (st**3)/3
#y = x
def f2(x):
    return x
def if2(st, fn):
    return (fn**2)/2 - (st**2)/2
#y = e**x
def f3(x):
    return np.exp(x)
def if3(st, fn):
    return np.exp(fn) - np.exp(st)

def error(real, numeric):
    return (abs(real - numeric)/real) * 100

#generacion de lista de datos en base a funcion
steps = 10
st = 0
fn = 10
#funciones a evaluar
fx = f3
ifx = if3 #integral de f1
x2 = np.linspace(st, fn, steps)
y2 = [fx(xi) for xi in x2]
int_real = ifx(x2[0], x2[-1]) / (max(x2) - min(x2))
err_real = error(int_real, int_real)
print("int sim = {}, error = {}%".format(int_real, err_real))

#obtención de integral por diferentes métodos de integración numérica
#promedio
prom = np.mean(y2)
prom_err = error(int_real, prom)
prom_list = [prom for i in range(0, steps)]
print("prom.  = {}, error = {}%".format(prom, prom_err))
#integral de simpson
simpson = itgrt.simps(y2, x2) / (max(x2) - min(x2))
simp_err = error(int_real, simpson)
sim_list = [simpson for i in range(0, steps)]
print("simpsn = {}, error = {}%".format(simpson, simp_err))

plt.plot(x2, y2)
plt.plot(x2, prom_list)
plt.plot(x2, sim_list)
plt.show()