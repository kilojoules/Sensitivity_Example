import chaospy
import chaospy as cp
import pandas as pd
import numpy as np

QUAD_ORDER = 18
quad = False

def f(x, y): return (1 - x) ** 2 * 10 * (y - x**2) ** 2

distribution = chaospy.J(
chaospy.Normal(0, 1),
chaospy.Normal(0, 1))

if quad:
   polynomial_expansion = cp.orth_ttr(QUAD_ORDER, distribution)
   X, W = chaospy.generate_quadrature(QUAD_ORDER, distribution, rule="G")
   evals = [f(x[0], x[1]) for x in X.T]
   foo_approx = cp.fit_quadrature(polynomial_expansion, X, W, evals)
else:
   dat = pd.read_csv('./dakota_tabular.dat', sep=r'\s+')
   polynomial_expansion = cp.orth_ttr(QUAD_ORDER, distribution)
   samples = np.array([dat.x1, dat.x2])
   evals = dat.response_fn_1
   foo_approx = cp.fit_regression(polynomial_expansion, samples, evals)

total = chaospy.descriptives.sensitivity.total.Sens_t(foo_approx, distribution)
main = chaospy.descriptives.sensitivity.main.Sens_m(foo_approx, distribution)
