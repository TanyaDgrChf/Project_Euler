import sys
from Problem16 import digital_root
sys.setrecursionlimit(100000)
def factorial(n):
    return rec_fac(n, 1)
def rec_fac(n, x):
    if n > 1:
        x *= n
        return rec_fac(n-1, x)
    else:
        return x
print(digital_root(factorial(100)))




