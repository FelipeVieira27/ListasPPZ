lista = []

for numero in range(1067, 3628):
    if numero %2 == 0 and numero %7 == 0:
        lista.append(numero)

print("Ao total, são: ",len(lista),"numeros")
print(lista)
