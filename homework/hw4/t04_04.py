import math


def f(x):
    return math.sin(x) - x / 3


def find_root():
    left = 1.6
    right = 3.0

    precision = 1e-10

    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) > 0:
            left = mid
        else:
            right = mid

    return round((left + right) / 2, 10)


root = find_root()
print("{0:.10f}".format(root))