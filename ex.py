import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np
def f(x, y): return (1 - x) ** 2 * 10 * (y - x**2) ** 2

def evalu(**kwargs):
   x = kwargs['cv']
   retval = dict(['fns':f(x[0], x[1])])
   return(retval)

if __name__ == '__main__':
   X = np.linspace(-3, 3, 100)
   Y = np.linspace(-3, 3, 100)
   Z = f(X[None, :], Y[:, None])
   #S = plt.contourf(X, Y, Z, 20)
   for ii in range(2):
      if ii == 0:
         S = plt.contourf(X, Y, np.log(Z), 20)
         plt.colorbar(label='log(Y)')
      else:
         S = plt.contourf(X, Y, Z, 20)
         plt.colorbar(label='Y')
      plt.xlabel('$x_0$')
      plt.ylabel('$x_1$')
      plt.savefig('YViz%i' % ii)
      plt.clf()
      plt.close('all')
