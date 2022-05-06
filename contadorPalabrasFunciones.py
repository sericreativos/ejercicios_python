
"""Función que cuenta el número de veces que aparece cada palabra en un texto.
Parámetros:
- text: Es una cadena de caracteres.
Devuelve: 
Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su 
frecuencia.
"""
text = 'Como quieres que te quiera, si el que quiero que me quiera no me quiere, como quiero que me quiera.'


def todoMinusculas(text):
    minusc=text.lower()
    return minusc

def textoLimpio(minusc):
    limp=minusc.replace(',',' ').replace('.',' ')
    separado=limp.split(" ")
    return separado

def contador(separado):
    diccionario={}
    for palabra in separado:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

minusc=todoMinusculas(text)
separado=textoLimpio(minusc)
count=contador(separado)

print(count)



