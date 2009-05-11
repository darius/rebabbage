def atan(x):
    "Hastings, _Approximations For Digital Computers_, p. 136"
    x2 = x * x
    return ((((.0208351*x2 - .0851330)*x2 + .1801410)*x2 - .3302995)*x2 + .9998660)*x

## atan(1)
#. 0.78540959999999993

# fp = 24-bit fixed point

def float_of_fp(x):
    return float(x) / (1 << 24)

def fp_lit(f):
    return int(f * (1 << 24))

def fp_mul(x, y):
    return (x * y) >> 24        # will this work for signed numbers?

c1 = fp_lit(.9998660)
c3 = fp_lit(-.3302995)
c5 = fp_lit(.1801410)
c7 = fp_lit(-.0851330)
c9 = fp_lit(.0208351)

def fp_atan(x):
    x2 = fp_mul(x, x)
    v = fp_mul(c9, x2) + c7
    v = fp_mul(v, x2) + c5
    v = fp_mul(v, x2) + c3
    v = fp_mul(v, x2) + c1
    v = fp_mul(v, x)
    return v

## float_of_fp(fp_atan(fp_lit(1.0)))
#. 0.78540951013565063

import math
## math.atan(1)
#. 0.78539816339744828

def tabulate(f, ref, lo, hi, dx):
    n = (hi - lo) / dx
    for i in range(int(n) + 1):
        x = lo + i * dx
        fx = f(x)
        error = fx - ref(x)
        print '%5.2f %8.5f %8.5f' % (x, fx, error * 1e5)

# tabulate(lambda x: float_of_fp(fp_atan(fp_lit(x))), atan, -1.0, 1.0, 0.01)

# tabulate(atan, math.atan, -1.0, 1.0, 0.01)

