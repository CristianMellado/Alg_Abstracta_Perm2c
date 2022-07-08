from utils.EUCLIDES import EUCLIDES
from utils.MILLER_RABIN import MILLER_RABIN
from utils.INVERSO import INVERSO
from utils.RSA import CIPHER

def __generate_primes(n):
    primes = ()
    for i in range(1, n):
        if EUCLIDES(i, n) != 1 and MILLER_RABIN(i, 500):
            primes += (i,)
            if len(primes) == 2:
                break

    return primes

def attack1():
    e = 65537
    n = 999630013489
    P = e, n
    c = 747120213790

    first, second = __generate_primes(n)
    
    phiN = (first - 1) * (second - 1)
    S = INVERSO(e, phiN), n

    m = CIPHER(c, S)
    cx = CIPHER(m, P)

    print("m: {:}\nc: {:}\nP(m) = cx: {:}".format(m, cx, c == cx))
