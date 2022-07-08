def POW_MOD(a, x, n):
    c = a % n
    r = 1
    
    while(x > 0):
        if((x % 2) != 0):
            r = (r * c) % n
        
        c = (c * c) % n
        x = int(x / 2)
    
    return r
