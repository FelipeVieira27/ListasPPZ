print ("Calcule aqui seu aumento salarial!")
atual = int(input("Insira seu salário atual: "))
porcentagem = int(input("Insira a porcentagem de aumento que deseja receber: "))
aumento = atual * porcentagem / 100
novo = atual + aumento
print (f"Seu novo salário será de: R${novo}")
