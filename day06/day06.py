from collections import Counter
import numpy as np

# data = [3, 4, 3, 1, 2]
data = np.loadtxt("input.txt", delimiter=",", dtype=int)
c = Counter(data)

for _ in range(256):
    new_c = Counter()
    for i in range(9):
        if i == 8:
            new_c[i] = c[0]
        elif i == 6:
            new_c[i] = c[i + 1] + c[0]
        else:
            new_c[i] = c[i + 1]
    c = new_c

print(sum(c.values()))

