n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O primeiro número é o maior: ", n1)
elif  n2 > n1 and n2 > n3:
    print("O segundo número é o maior: ", n2)
elif n3 > n2 and n3 > n1:
    print("O terceiro número é o maior: ", n3)
else:
    print("Tente novamente com números que não sejam iguais")
