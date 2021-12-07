import numpy as np

# part1
l = np.loadtxt("input.txt", dtype=str)
ll = [list(map(int, list(x))) for x in l]
ll = np.array(ll, dtype=int)
ll = 1 * (ll.sum(axis=0) / ll.shape[0] > 0.5)
int("".join(map(str, ll)), 2) ^ int("1" * len(l[0]), 2)
