# Alg_Abstracta_Perm_02c

- Cristian Mellado Baca


Correr el main.py
Use el modulo hashlib y sys de python, ademas de los codigos anteriores (como el de euclides, miller rabin, generar primos, cipher, etc)


## Ataque 1

1.  (5 points) Si m es el mensaje y c es el cifrado (ambos representados por un entero). Y ademas, la clave publica es P = {e, n} (en ese orden). Hallar m cuando:
    P  =  {65537, 999630013489}    y    c  =  747120213790

Primero hay que encontrar p y q que multiplicados dan n, ya teniendo p y q se puede hallar phi(n). Al hallar phi(n) se puede hallar la llave secreta y descifrar c.

```py
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
```
## Ataque 2

2.  (7 points) Si m es el mensaje y c es el cifrado (ambos representados por un entero). Y ademas, la clave publica es P = {e, n} (en ese orden). Hallar m cuando:
    P = {7, 357942341797258687749918078325684554030037780242282261 93532908190484670252364677411513516111204504060317568667}
    c = 35794234179725868774991807832568455403003778024228226193 532908190484670252364677411513516052471686245831933544
Sin embargo al enviar el mismo mensaje (m) cuando e = 11, el cifrado resulto ser
    c = 357942341797258687749918078325684554030037780242282261935329081 90484670252364665786748759822531352444533388184.

Como ya se tiene un mensaje cifrado dos veces con diferentes exponentes pero mismo módulo, se puede hacer un ataque de modulo comun.

```py
def attack2():
    e = 7
    n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
    P = e, n
    c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
    
    e_ = 11
    P_ = e_, n
    c_ = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

    if (EUCLIDES(e, e_ == 1) and EUCLIDES(c_, n)):
        __message_module_attack()

        z, x, y = EUCLIDES_EXTEND(e, e_)

        a = EXP_MOD(INVERSO(c, n), -x, n) if x < 0 else EXP_MOD(c, x, n)
        b = EXP_MODBITS(INVERSO(c_, n), -y, n) if y < 0 else EXP_MODBITS(c_, y, n)

        m = (a * b) % n
        cx = CIPHER(m, P)
```
## Ataque 3

3.  (8 points) Validar ﬁrmas digitales: Veriﬁcar que P (S(m)) = HASH(M ) para 3 mensajes distintos, mostrando la respectiva ﬁrma σ en cada caso. Utilice la Funci´on Hash SHA-1 para generar m a trav´es de un texto M ( por ejemplo Hola Mundo). Utilizar b = 32 bits en el algoritmo RSA.

Se generan dos claves RSA (P y S) y se asigna m = HASH(M) % P[1] (n), luego se usa RSA para cifrar y descifrar m, asi estaria validando su autenticidad.

```py
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
```

### Resultado

```bash
-------- ATAQUE 1 --------

m: 100000000001
c: 747120213790
P(m) = cx: True

-------- ATAQUE 2 --------

Posible ataque de modulo

m: 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568000
cx: 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
c: 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
cx = c: True

-------- ATAQUE 3 --------

M: b'Hello World!'
m: 475123918
sign: 417705249
u: 475123918
u = m: True  
```

## Punto adicional para el examen final:
Utilizar el algoritmo RSA (b = 32) para generar y validar una ﬁrma digital. Utilizar el estandar PKCS #1 v1.5 para a˜nadir un padding al mensaje original. Fecha lımite de entrega: 08/07/22.

```py
from resources.rsa import RSA
from resources.randomgen_primos import RANDOMGEN_PRIMOS
import hashlib, sys

def gen_EB(M, bits):
  H = hashlib.sha1(bytes(M, encoding="utf-8")).hexdigest()
  PS = "F" * (bits - sys.getsizeof(H) - 3)
  T = hex(RANDOMGEN_PRIMOS(bits, 100))[2:] + H
  return "0001" + PS + "00" + T


def StringToInt(EB):
  return int(EB, base=16)


def IntToString(c):
  return hex(c)[2:]

bits = 32
rsa = RSA(bits)

EB = gen_EB("Hola mundo", bits)
m = StringToInt(EB)
c = rsa.Descifrado(m)
OB = IntToString(c)

print("\"m\" inicial para cifrar: ", m % rsa.n)
print("Firma digital:", OB)
print("\"m\" final descifrado: ", rsa.Cifrado(c))

```
### Resultado
```bash
"m" inicial para cifrar:  1481651286
Firma digital: 76cda0f1
"m" final descifrado:  1481651286
```
