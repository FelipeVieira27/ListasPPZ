numero = int(input("Insira um valor: "))

a, b = 1, 1
inicio = 1

while inicio <= numero-2:
    a, b = b, a + b
    inicio = inicio + 1

print ("O correspondente deste valor é", b)
