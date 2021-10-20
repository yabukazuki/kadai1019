import numpy as np
from scipy import linalg

a = np.array([[3, 5], [4,7]])
print(a)
print(np.linalg.inv(a))

b = np.array([[2,1,3], [4,5,4], [3,1,5]])
print(b)
print(np.linalg.inv(b))
