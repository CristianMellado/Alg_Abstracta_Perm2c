def EXP_MODBITS(x, y, z):
    c = 0
    d = 1
    n = y.bit_length()
    for i in range(n):
        c = 2 * c
        d = (d * d) % z
        if y & 2 ** (n - 1):
            c += 1
            d = (d * x) % z
        y = y << 1
    return 
