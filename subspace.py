import pandas as pd
import active_subspaces as ac
import numpy as np
import matplotlib.pyplot as plt
dat = pd.read_csv('./dakota_tabular.dat', sep=r'\s+')
XX = np.hstack((dat.x1.values[:, None], dat.x2.values[:, None]))
#XX = np.hstack((dat.x1.T, dat.x2.T))
f = dat.response_fn_1.values
f = f.reshape(f.size, 1)
#Instantiate a subspace object
ss = ac.subspaces.Subspaces()

#Compute the subspace with a global linear model (sstype='OLS') and 100 bootstrap replicates
ss.compute(X=XX, f=f, nboot=100, sstype='OLS')
#This plots the eigenvalues (ss.eigenvals) with bootstrap ranges (ss.e_br)
ac.utils.plotters.eigenvalues(ss.eigenvals, ss.e_br)
plt.savefig('eigenvals')
plt.clf()
#This plots subspace errors with bootstrap ranges (all contained in ss.sub_br)
ac.utils.plotters.subspace_errors(ss.sub_br)
plt.savefig('errors')
plt.clf()

#This makes sufficient summary plots with the active variables (XX.dot(ss.W1)) and output (f)
ac.utils.plotters.sufficient_summary(XX.dot(ss.W1), f)
plt.savefig('summary')
plt.clf()
