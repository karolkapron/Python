import numpy as np
from typing import List



def is_latin(s):
    array = np.array(s)
    array_transpose = array.transpose()
    for el in array:
        if len(el) != len(set(el)):
            return False
    for el_ in array_transpose:
        if len(el_) != len(set(el_)):
            return False
    return True


def latin_square(n):
    row = [i for i in range(1, n + 1)]

    return [row[i:] + row[:i] for i in range(n)]


if __name__ == '__main__':
    n = int(input("Podaj liczbe kolumn/wierszy: "))
    print(np.array(latin_square(n)))