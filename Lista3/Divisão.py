valor1 = int(input("Insira o primeiro número: "))
valor2 = int(input("Insira o segundo número: "))

while valor1 % valor2 > 0:
    valor1, valor2 = valor2, valor1 % valor2

print("O mínimo divisor comum entre estes números é: ", valor2)
