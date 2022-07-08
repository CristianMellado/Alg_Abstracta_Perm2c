from hashlib import sha1
from resources.rsa import RSA_KEY_GENERATOR, CIPHER

def attack3():
    k = 32
    P, S = RSA_KEY_GENERATOR(k)
    _, n = P
    M = b'Hello World!'

    h = sha1()
    h.update(M)
    m = int(h.hexdigest(), 16)
    m %= n

    sign = CIPHER(m, S)
    u = CIPHER(sign, P)

    print("M: {:}\nm: {:}\nsign: {:}\nu: {:}\nu = m: {:}".format(M, m, sign, u, u == m))
