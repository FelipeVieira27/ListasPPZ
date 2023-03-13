nome = input("Insira o seu usuário: ")
senha = input("Insira sua senha: ")

while nome == senha:
    print("Erro, seu usuário não pode ser igual a sua senha")
    nome = input("Insira o seu usuário: ")
    senha = input("Insira sua senha: ")

print("Você se cadastrou com sucesso!")
