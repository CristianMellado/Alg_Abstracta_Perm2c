from utils.RANDOMINTEGER import RANDOMINTEGER
from utils.ES_COMPUESTO import ES_COMPUESTO

def MILLER_RABIN(n, s):
    t = 0
    u = n - 1
    while (u % 2 == 0):
        u = u / 2
        t = t + 1

    j = 1
    while (j < s):
        a = RANDOMINTEGER(2, n - 1)
        if (ES_COMPUESTO(a, n, t, u)):
            return False
            
        j += 1

    return True
