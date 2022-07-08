# Alg_Abstracta_Perm_02c

- Cristian Mellado Baca

### Ejecución

Correr el main.py. en la terminal, ejecutara el ataque 1, 2 y 3

```bash
python main.py
```

## Ataques al Algoritmo RSA

# Ataque 1

Para hallar el mensaje m primero hay que encontrar cuales son los números primos p y q que multiplicados dan n. En este caso específico, es posible dado que el número no es muy grande. Entonces podemos hallar phi(n) con estos dos números p, q.  Al hallar phi(n) podemos hallar la llave secreta y descifrar c.

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
# Ataque 2

Como ya tenemos un mensaje cifrado dos veces con diferentes exponentes pero mismo módulo, se puede hacer un ataque de modulo comun. Se hallan los valores de x , y mediante el algoritmo Extendido de Euclides. Como e_1 * x + e_2 * y = 1 --> c1^x * c2^y mod n = m --> (x es menor que 0) --> c1_inversa^x * c2^y mod n

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
# Ataque 3

Se comprueba que P(S(m)) = HASH(M), siendo M un mensaje, la función HASH sha1, la función P RSA con la clave pública y la funcion S RSA con la clave secreta. Se generan dos claves RSA (P y S) y se asigna m = HASH(M) % P[1] (n), luego se usa RSA para cifrar m (y luego descifrarlo). Este procedimiento es común en firmas digitales para revisar la autenticidad de un archivo.

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

## Resultado

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
