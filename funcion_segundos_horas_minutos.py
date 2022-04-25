"""Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.

La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
convertir a horas,minutos y segundos o salir del programa."""

def conversionAsegundos(horas,minutos,segundos):
    horas=int(horas*3600)
    minutos= int(minutos*60)
    segundosR=segundos
    conver=horas+minutos+segundosR 
    return conver    



def conversionAhorasMinSeg(segundos):
    
    horas= int(segundos/3600)
    segundos=segundos-horas*3600
    
    minutos=segundos/60
    segundos=segundos-minutos*60

    segundosR=segundos

    return horas,minutos,segundosR



while True:
    opciones = input("MENU DE CONVERSIONES:  Presiona 1. Convertir de  Horas, minutos y segundos a Segundos  Presiona 2. para convertir de segundos a Horas, Minutos y Segundos. Presiona ENTER  para continuar ó Presiona 0 para salir ")
    
    if opciones == str(1):
        hor= int (input("ingresa cuantas horas: "))
        min=  int (input("ingresa cuantos minutos: "))
        sec=  int (input("ingresa cuantos segundos: "))
        print("Son " , conversionAsegundos(hor, min, sec)," segundos")

    if opciones==str(2):
        seconds=int(input("ingresa cuantos segundos quieres convertir a horas: "))
        hour,minute,second= conversionAhorasMinSeg(seconds)
        print("Horas: ", hour,"minutos: ", minute, "segundos: ", seconds)
    
    if opciones==str(0):
        print("Estas saliendo del sistema ")
        break




