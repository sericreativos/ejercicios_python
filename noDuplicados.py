"""Sea una lista con palabras, escribir un programa para eliminar los elementos duplicados en la lista conservando el orden de los elementos.
Ejemplo: miLista= ['uno', 'dos', 'tres', 'uno', 'cuatro']
        resultado= ['uno','dos', 'tres', 'cuatro']"""

def noDuplicar(listaNueva):
    listaNueva=[]
    miLista= ['uno', 'dos', 'tres', 'uno', 'cuatro','cinco','cinco','uno']

    for elemento in miLista:
        if elemento not in listaNueva:
            listaNueva.append(elemento)
    print(listaNueva)
noDuplicar([])

