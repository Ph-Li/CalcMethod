# -*- coding: utf-8 -*-


def steffensen(f, x0, tol):
    if tol <= 0:
        print("illegal value for tolerance")
        return

    for i in range(1, 1000):
        y0 = f(x0)
        x = x0 - y0 * y0 / (f(x0 + y0) - y0)
        if abs(x - x0) < tol:
            print("found root", x, "in", i, "iteration(s)")
            return
        x0 = x
    print("failed to converge in 1K iterations")


def steffensen_atk(f, x0, tol):
    """This function takes as inputs: a fixed point iteration function, f,
    and initial guess to the fixed point, p0, and a tolerance, tol.
    This function will calculate and return the fixed point, p,
    that makes the expression f(x) = p true to within the desired
    tolerance, tol.
    """

    if tol <= 0:
        print("illegal value for tolerance")
        return

    # do a large, but finite, number of iterations

    for i in range(1, 1000):
        x1 = f(x0)        # calculate the next two guesses for the fixed point
        x2 = f(x1)
        # use Aitken's delta squared method to find a better approximation to
        # p0
        x = x2 - (x2 - x1) * (x2 - x1) / (x2 - 2 * x1 + x0)
        if abs(x - x0) < tol:
            print("found root", x, "after", i, "iteration(s)")
            return
        x0 = x
    print("failed to converge in 1K iterations")
