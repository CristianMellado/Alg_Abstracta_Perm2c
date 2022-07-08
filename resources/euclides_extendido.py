def EUCLIDES_EXTENDIDO(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, dx, dy) = EUCLIDES_EXTEND(b, a % b)
        (x, y) = (dy, dx - a // b * dy)
        return (d, x, y)
