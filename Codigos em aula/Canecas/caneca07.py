import urllib.request
preço = 99.99
x = 1
while preço >= 4.75:
    pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
    texto = pagina.read().decode('utf8') 
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    preço = float(texto[inicio:fim])
print (f'Comprar: R$ {preço:.2f}')

