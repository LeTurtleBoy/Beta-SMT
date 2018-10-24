import codecs

cipher_text = codecs.encode("hola mundo 1 2 3 4 5 6 7 8 9 ", 'rot_13')
print(cipher_text)
print(codecs.decode(cipher_text,'rot_13'))

#Test
