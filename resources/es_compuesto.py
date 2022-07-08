import math
from utils.POW_MOD import POW_MOD

def ES_COMPUESTO(a, n, t, u):
    x = POW_MOD(a, u, n)

    if (x == 1 or x == n - 1):
        return False

    for i in range(1,t,1):
        x = POW_MOD(x, 2, n)
        if (x == n - 1):
            return False

    return True
