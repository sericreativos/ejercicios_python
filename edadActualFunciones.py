"""Dados el nombre y el año de nacimiento d euna persona, implementar la clase Persona y crear 
el objeto que muestre en pantalla la edad actual de esa persona. 
Los atributos y metodos de la clase son:
___________________
Persona                 Clase
___________________
Nombre                  Atributo(s)
Año_de_nacimiento       de 
___________________     instancia
Edad_actual()           Metodos
"""
from time import strftime
from datetime import date
import datetime

class Persona():
    def edad_actual(nombre, año_de_nacimiento,calcularEdadActual):
        nombre=input("Ingresa tu nombre: ")
        año_de_nacimiento=int(input("Ingrea tu año de nacimiento: "))
        #esto es una funcion para obtener el año actual importando datetime
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        calcularEdadActual=int(year)-año_de_nacimiento
        print("Hola ", nombre, "tu edad actual es ", calcularEdadActual, "años de edad")
        return calcularEdadActual
    edad_actual("",2013,9)
