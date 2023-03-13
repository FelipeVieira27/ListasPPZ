ano = 0
PaisA = 80000
PaisB = 200000

while PaisA < PaisB:
    ano = ano + 1
    print(f"Ano: {ano + 1}")
    PaisA = PaisA * 1.03
    print(f"País A: {PaisA:.0f}")
    PaisB = PaisB * 1.015
    print(f"País B: {PaisB:.0f}")

print("Foram necessários", ano + 1, "anos para o País A ultrapassar o País B")
