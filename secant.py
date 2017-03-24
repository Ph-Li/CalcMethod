# -*- coding: utf-8 -*-


def secant(f, a, b, tol):
    if tol <= 0:
        print("illegal value for tolerance")
        return

    i = 0
    while abs(b - a) >= tol:
        c = b - ((b - a) / (f(b) - f(a))) * f(b)
        a = b
        b = c
        i = i + 1
    print("Found root is", c, "after", i, "iteration(s)")
