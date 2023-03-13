nota = float(input("Insira sua nota entre 0 e 10: "))

while nota < 0 or nota > 10:
  print ("Insira novamente a nota: ")
  nota = float(input("Insira sua nota entre 0 e 10: "))

if nota >= 7 and nota <= 10:
    print ("Parabéns, você foi aprovado!")
if nota >= 0 and nota < 7:
    print ("Você não foi aprovado :(")
