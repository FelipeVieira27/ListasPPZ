import urllib.request
pagina = urllib.request.urlopen(
         'http://beans.itcarlow.ie/prices.html') 
texto = pagina.read().decode('utf8') 
preço = texto[233:238]
print (preço)

