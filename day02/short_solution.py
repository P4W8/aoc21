import numpy as np

data = np.loadtxt('input.txt', delimiter='\n', dtype=int)

h = d = a = 0

for x in data:
  match x.split():
    case 'forward', n:
      h += int(n)
      d += int(n)*a
    case 'up', n:
      a -= int(n)
    case 'down', n:
      a += int(n)

print(h*a, h*d)