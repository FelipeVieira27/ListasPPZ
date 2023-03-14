import random
numeros = random.sample(range(1, 100), 20)
print ("Este são os números sorteados", numeros)
par = [ ]
impar = [ ]
k = 1
while k < 100:
    if k in numeros and k%2 == 0:
        par.append(k)
    if k in numeros and k%2 != 0:
        impar.append(k)
    k = k + 1
print("Estes são os pares: ", par)

print("Estes são os ímpares: ",impar)
    

