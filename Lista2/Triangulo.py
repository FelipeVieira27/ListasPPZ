lado1 = int(input("Insira o primeiro lado do triângulo: "))
lado2 = int(input("Insira o segundo lado do triângulo: "))
lado3 = int(input("Insira o terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Estas medidas formam um triângulo equilátero")
elif lado1 == lado2 and lado3 < lado1 + lado2:
    print("Estas medidas formam um triângulo isóceles")
elif lado1 == lado3 and lado2 < lado1 + lado3:
    print("Estas medidas formam um triângulo isóceles")
elif lado3 == lado2 and lado1 < lado3 + lado2:
    print("Estas medidas formam um triângulo isóceles")
elif lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print("Estas medidas não formam um triângulo")
else: print("Estas medidas formam um triângulo escaleno")
