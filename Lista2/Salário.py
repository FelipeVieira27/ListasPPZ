salariohora = float(input("Insira o valor que você recebe por hora: "))
horas = int(input("Insira a quantidade de horas trabalhadas por mês: "))
bruto = salariohora * horas
imposto = bruto * 11 / 100
inss = bruto * 8 / 100
sindicato = bruto * 5 / 100
salario = bruto - imposto - inss - sindicato
print("Seu salário bruto é de R$: ", bruto)
print(f"R$: {imposto:.2f} foram para o imposto de renda") 
print(f"R$: {inss:.2f} foram para o INSS")
print(f"R$: {sindicato:.2f} foram para o sindicato")
print(f"No final, você ficou com R$:{salario:.2f}")
