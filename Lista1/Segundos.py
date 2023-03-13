dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))
tempo = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print (f"Seu tempo é de {tempo} segundos")
