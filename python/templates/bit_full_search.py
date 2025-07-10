from itertools import product

n = 3
for i in product(*[range(2) for _ in range(n)]):
    print(i)
