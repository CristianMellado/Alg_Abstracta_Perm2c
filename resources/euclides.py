def EUCLIDES(a, b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a % b)
      
