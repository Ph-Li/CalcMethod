# -*- coding: utf-8 -*-

"""INPUT: Function f, endpoint values a, b, tolerance TOL
CONDITIONS: a < b, either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
"""

from math import log2
from math import copysign


def bisect(f, a, b, tol):
    if tol <= 0 or tol > b - a:
        print("illegal value for tolerance")
        return

    # limit iterations to prevent infinite loop

    m = log2(b - a) - log2(tol)
    if m > 1000:
        print("failed to find root in 1K iterations")

    i = 0
    while i <= m:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if copysign(1, f(c)) == copysign(1, f(a)):
            a = c
        else:
            b = c
        i = i + 1
    print("Found root is", c, "after", i, "iteration.")
