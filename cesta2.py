"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el articulo y su precio y aañadir el par al diccionario, hasta que el usuario decida 
terminar.

Despues se debe mostrar por pantalla la lista de la compra y el coste total, con el 
siguiente formato

Lista de la compra
Articulo1   Precio
Articulo2   Precio
Articulo3   Precio
...         ...
Total       Coste
"""
cestaCompra={}
total=0

while True:
    articulo=input("Ingrese un Articulo: ")
    precio=float (input("Ingrese el precio del Articulo: "))
    cestaCompra[articulo]=precio

    terminar=input("Si deseas terminar tu compra, presiona <t> , continuar <Enter>")
    if terminar=="t":
        break

print("Articulo,      Precio")
for articulo in cestaCompra:
    prec=cestaCompra[articulo]
    print(articulo   , "  ",   prec)
    total += prec

print("total " ,   total)





