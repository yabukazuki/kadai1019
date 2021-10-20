import numpy as np

a=np.random.randint(0,9,(1,9))
b=np.random.randint(0,9,(1,9))
print(a)
print(b)
print(a==b)
c=a==b
print(c)
print(np.count_nonzero(c==True))
