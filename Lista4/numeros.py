import random
numeros = random.sample(range(1, 100), 10)
print ("Este são os números sorteados", numeros)
lista = []
k = 1
while k < 100:
    if k in numeros:
        lista.append (k)
    k = k + 1
print ("O maior número é:", lista[-1],"e o menor é:",lista[0])
    

