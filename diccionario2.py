"""Escribir un programa que cree un diccionario de traduccion español-ingles. El usuario 
introducira las palabras en español e ingles separados por los dos puntos, y cada par 
<palabra>:<traduccion> separados por comas. 

El programa debe crear un diccionario con las palabras y sus traducciones. 

Despues pedira una frase en español y utilizara el dicccionario para 
traducirla palabra a palabra. Si una palabra no esta en el dicccionario debe dejarla sin traducir"""

diccionario={}
parPalabras=input("ingresa una palabra en español y su significado en ingles <español>:<ingles>")

for i in parPalabras.split(","):
    clave,valor=i.split(":")
    diccionario[clave]=valor

frase=input("ingresa la frase a traducir: ")

for i in frase.split(" "):
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')




    


    
