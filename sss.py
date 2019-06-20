from scipy.interpolate import griddata
import numpy as np
def f(x, y): return (1 - x) ** 2 * 10 * (y - x**2) ** 2
X = np.linspace(-3, 3)
Y = np.linspace(-3, 3)
Z = f(X, Y)
xi = np.linspace(X.min(), X.max(), 1000)
yi = np.linspace(Y.min(), Y.max(), 1000)
zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')
