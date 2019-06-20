import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dat = pd.read_csv('./sobs.txt', sep=r'\s+') 
W = 0.3
x = np.array([0, 1])
f, ax = plt.subplots()
ax.bar(x - .5 * W, dat.Main, width=W, label='Main')
ax.bar(x + .5 * W, dat.Total, width=W, label='Total')
ax.legend()
ax.set_xticks(x)
ax.set_xticklabels(dat.variable.values)
#ax.set_yscale('log')
ax.set_ylabel('sobol index')
plt.savefig('sobBars')
plt.clf()
plt.close('all')
