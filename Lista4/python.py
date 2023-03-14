texto = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you'''
texto = texto.replace(",", " ")
texto = texto.replace("."," ")
texto = texto.lower()
texto = texto.split()

for palavra in texto:
    if palavra[0] or palavra[-1] in "python":
        print (palavra)
