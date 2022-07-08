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
c = rsa.Descifrado(m)  # m^d mod n
OB = IntToString(c)

print("\"m\" inicial para descifrar: ", m % rsa.n) 
print("Firma digital:", OB)
print("\"m\" final descifrado: ", rsa.Cifrado(c))
