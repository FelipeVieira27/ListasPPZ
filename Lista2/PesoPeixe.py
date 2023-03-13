peso = float(input("Insira o peso do peixe em Kg: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print (f"Você deverá pagar R$:{multa:.2f} por {excesso}Kg a mais que o regulamento")
