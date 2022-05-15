import route_opt as ropt
import numpy as np

# [[0,  1,  3,  2,  3],
#  [1,  0,  2,  1,  2],
#  [2,  1,  0,  1,  2],
#  [3,  2,  1,  0,  1],
#  [4,  3,  2,  1,  0]]

# [[1,  3,  105,21, 231],
#  [2,  1,  35, 7,  77],
#  [6,  3,  1,  7,  77],
#  [30, 15, 5,  1,  11],
#  [210,105,35, 7,  1]]

a = np.array([[0,      1,      np.inf, np.inf, np.inf],
              [1,      0,      np.inf, 1,      np.inf],
              [np.inf, 1,      0,      1,      np.inf],
              [np.inf, np.inf, 1,      0,      1],
              [np.inf, np.inf, np.inf, 1,      0]])

primes = ropt.list_primes(a.shape[0])

print(primes)

print(ropt.iterate_mat(a, primes))
