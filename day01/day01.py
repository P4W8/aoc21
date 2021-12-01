import numpy as np

data = np.loadtxt("input.txt", dtype=int)
print(np.sum(data[1:] > data[:-1]))
print(np.sum(data[3:] > data[:-3]))
