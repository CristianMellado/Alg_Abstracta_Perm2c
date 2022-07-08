from resources.euclides import EUCLIDES
from resources.euclides_extendido import EUCLIDES_EXTENDIDO
from resources.exp_mod import EXP_MOD
from resources.exp_modbits import EXP_MODBITS
from resources.inverso import INVERSO
from resources.rsa import CIPHER

def __message_module_attack():
    print("Posible ataque de modulo comun")

def attack2():
    e = 7
    n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
    P = e, n
    c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
    
    e_ = 11
    P_ = (e_, n)
    c_ = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

    if (EUCLIDES(e, e_ == 1) and EUCLIDES(c_, n)):
        __message_module_attack()

        z, x, y = EUCLIDES_EXTEND(e, e_)

        a = EXP_MOD(INVERSO(c, n), -x, n) if x < 0 else EXP_MOD(c, x, n)
        b = EXP_MODBITS(INVERSO(c_, n), -y, n) if y < 0 else EXP_MODBITS(c_, y, n)

        m = (a * b) % n
        cx = CIPHER(m, P)

        print("\nm: {:}\ncx: {:}\nc: {:}\ncx = c: {:}".format(m, cx, c, cx == c))
    else:
        print("useless!")
