import math
from utils.RANDOMINTEGER import RANDOMINTEGER

def RANDOMBITS(b):
    max = pow(2, b) - 1
    n = RANDOMINTEGER(0, max)
    m = pow(2, b - 1) + 1
    n = n | m
    return 
