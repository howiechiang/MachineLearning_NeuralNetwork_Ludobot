from core01_HillClimber import *
import numpy as np


a = MatrixCreate(5, 5)
a = MatrixRandomize(a, -1, 1)
b = MatrixCreate(5, 5)
b = MatrixRandomize(b)

print(a)
print(b)
print(a * b + np.logical_not(b))

#print(1.0*np.array(np.logical_not(b)))