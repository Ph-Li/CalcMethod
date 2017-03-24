# -*- coding: utf-8 -*-


def picard(x0, f, tol):
    if tol <= 0:
        print("illegal value for tolerance")
        return

    for i in range(1, 1000):
        x = f(x0)
        if abs(x - x0) < tol:
            print("found root", x, "after", i, "iteration(s)")
            return
        x0 = x
    print("failed to find root in 1K iterations")
