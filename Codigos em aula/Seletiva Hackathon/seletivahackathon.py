def hack (n, k):
    lista = []
    for k in range (2**n):
        lista.append (bin(k))
    def um(x):
        return x.count("1")
    lista.sort(key=um, reverse=True)
    return lista
