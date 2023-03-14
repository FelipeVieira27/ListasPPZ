sorte = []
for numero in range(18644, 33088):
    if "2" in str(numero) and "7" not in str(numero):
        sorte.append(numero)
print("Ao total são: ", len(sorte),"números")
        
