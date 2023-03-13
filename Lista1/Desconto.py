print ("Calcule desconto aqui!")
produto = float(input("Insira o valor original do produto: "))
desconto = float(input("Insira o desconto do produto: "))
valor1 = produto * desconto / 100
valor2 = produto - valor1
print ("Seu produto sairá por R$:", valor2)
print ("Com um desconto de R$:", valor1)
