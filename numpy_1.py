import numpy as np
import math


a = np.array([1,2,3])
print(a)
print(a.ndim)
print(a.shape)

b = np.array([ [1,2,3],[4,5,6] ])
print(b)
print(b.shape)


d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)

a = np.array([ [1,1],[0,1] ])
b = np.array([ [2,0],[3,4] ])
print(a*b)
print(a@b)  #matrix-level operations @ sign

b = np.arange(1,16,1).reshape(3,5)
print(b)