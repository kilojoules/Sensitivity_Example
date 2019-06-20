import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 1])
f, ax = plt.subplots()
ax.bar(x, [0.93232686 **2, 0.36161669 ** 2])
ax.set_xticks(x)
ax.set_xticklabels(['x0', 'x1'])
ax.set_ylabel('$a_i^2$')
plt.savefig('aaBars')
plt.clf()
plt.close('all')
