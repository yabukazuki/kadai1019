import numpy as np
from scipy import linalg # scipy.linalg のインポート

a = np.array([[2,1,3], [4,5,4], [3,1,5]])
b = np.array([0,-2,1])

a_inv = np.linalg.inv(a)
print(a_inv)
print(a@a_inv)
print(np.dot(a_inv,b))


lu, p = linalg.lu_factor(a)

print(lu) # 上三角部分が U, 下三角部分（対角成分除く）が L
print(p)

print(linalg.lu_solve((lu,p), b))

a = np.array([[8,16,24,32],[2,7,12,17],[6,17,32,59],[7,22,46,105]])
b = np.array([160,70,198,291])

a_inv = np.linalg.inv(a)
print(a_inv)
print(a@a_inv)
print(np.dot(a_inv,b))

lu, p = linalg.lu_factor(a)

print(lu) # 上三角部分が U, 下三角部分（対角成分除く）が L
print(p)

print(linalg.lu_solve((lu,p), b))


