texto = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you.'''
texto = texto.lower()
texto = texto.replace(",", " ").replace(":"," ").replace("."," ")
lista = []
texto = texto.split()

def possui(palavra):
    for letra in palavra:
        if letra in str("python"):
            return True
    return False

for palavra in texto:
    if possui(palavra) and len(palavra) > 4 :
        lista.append(palavra)

print("No total, são ",len(lista),"palavras.")
print(lista)
