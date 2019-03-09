from matplotlib import pyplot as plt
import numpy as np
import math

def object_func(x, y):
    return x * y

def constrain_func1(x):
    return math.sqrt(9 - x**2)

def constrain_func2(x):
    return -x**2

x1 = np.arange(-10, 11, 0.02)
x2 = x1[:]
candidates = dict()
for x in x1:
    for y in x2:
        if (x + y**2 <= 0) and (x**2 + y**2 <= 9):
            f = object_func(x, y)
            candidates[(x, y)] = f

min_f = 10e10
opt_x = tuple()
for k, v in candidates.items():
    if v < min_f:
        min_f = v
        opt_x = k

print(opt_x, min_f)


