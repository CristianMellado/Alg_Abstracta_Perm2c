from utils.RANDOMGEN_PRIMOS import RANDOMGEN_PRIMOS
from utils.RANDOMBITS import RANDOMBITS
from utils.EUCLIDES import EUCLIDES
from utils.INVERSO import INVERSO
from utils.EXP_MOD import EXP_MOD

def RSA_KEY_GENERATOR(bits):
    arg = bits // 2
    p = RANDOMGEN_PRIMOS(arg)
    q = RANDOMGEN_PRIMOS(arg)
    while p == q:
        q = RANDOMGEN_PRIMOS(arg)

    n = p * q
    phiN = (p - 1) * (q - 1)
    
    e = RANDOMBITS(bits)
    while EUCLIDES(e, phiN) != 1:
        e = RANDOMBITS(bits)
    
    d = INVERSO(e, phiN)
    return (e, n), (d, n)

def CIPHER(m, k: tuple):
    arg1, arg2 = k
    return EXP_MOD(m, arg1, arg2)
