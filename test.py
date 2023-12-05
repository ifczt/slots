import random

import numpy as np


def generate_array(i,j):
    index = random.randint(1, 100)
    return index+j-j


rows = 3
cols = 3

matrix = np.fromfunction(generate_array, (rows, cols), dtype=int)
np.array()
print(matrix)
