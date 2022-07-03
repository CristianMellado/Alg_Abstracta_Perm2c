import hashlib
h = hashlib.sha1()
rsa = RSA(32)   # 32 bits

print(" m\t\t\t|\t c = S(m)\t\t|\t Hash(m)\t\t\t|\t m = P(S(m))")
print("-"*125)

words = ["Hola Mundo", "Juego de Monos", "pichanga fiufiu"]
for word in words:
  rsa_word, data = rsa.Cifrado_msg(word)

  h.update(bytes(word, encoding="utf-8"))
  hash_word = h.hexdigest()

	
  rsa_word_2 = rsa.Descifrado_msg(rsa_word, data)

  print(word + " "*(25-len(word)) + rsa_word + " "*(32-len(rsa_word)) + hash_word + " "*10 + rsa_word_2)
