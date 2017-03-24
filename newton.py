# -*- coding: utf-8 -*-

"""Args:
    x0: The initial value
    f(x): The function whose root we are trying to find
    g(x): The derivative of f(x)
    tol: Accuracy desired
"""


def newton(x0, f, g, tol):
    if tol <= 0:
        print("illegal value for tolerance")
        return

    for i in range(1, 1000):
        x1 = x0 - f(x0) / g(x0)        # Do Newton's computation
        if abs(x1 - x0) < tol:
            print("found root", x1, "after", i, "iteration(s)")
            return
        x0 = x1
    print("failed to find root in 1K iterations")
