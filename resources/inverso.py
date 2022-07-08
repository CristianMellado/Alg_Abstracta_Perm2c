from utils.EUCLIDES_EXTENDIDO import EUCLIDES_EXTENDIDO

def INVERSO(a, n):
    (mcd, x, y) = EUCLIDES_EXTENDIDO(a, n)
    if mcd == 1:
        return x % n
    else:
        return None
