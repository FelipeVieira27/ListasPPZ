Cigarros = int(input("Quantos cigarros você fuma por dia? "))
Tempo = int(input("Por quantos anos você fuma? "))
Totalcigarros = Tempo*365*Cigarros
Totaltempo = Totalcigarros/144
print (f"Ao decorrer de {Tempo} ano(s), você já perdeu {Totaltempo:.0f} dias de vida")
