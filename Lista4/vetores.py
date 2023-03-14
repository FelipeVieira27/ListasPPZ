import random

vet1 = random.sample(range(1, 100), 10)
vet2 = random.sample(range(1, 100), 10)
vet3 = [ ]
k = 0
while k < 100:
    if k in vet1 or k in vet2:
        vet3.append (k)
    k = k + 1
    
print("Este é o primeiro vetor: ", vet1)
print("Este é o segundo vetor: ", vet2)

print("Este é o terceiro vetor: ", vet3)
