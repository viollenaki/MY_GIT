from random import randint
from time import time
matrix = [[randint(1,100) for _ in range(1000)] for _ in range(1000)]

t = time()
dict_rows = {}
for i in range(1000):
    dict_rows[i] = sum(matrix[i])
print(time() - t)

t = time()
dict_column = {}
for i in range(1000):
    dict_column[i] = sum([matrix[j][i] for j in range(1000)])
print(time() - t)

