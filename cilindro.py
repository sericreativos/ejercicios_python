"""desarrollar un programa que contenga una clase cilindro y contenga los siguientes atributos 
y metodos:
_____________
cilindro        Clase
_____________
Pi              Atributo(s) de clase 
-------------
radio           Atributo(s) de instancia
altura
-------------
Superficie()    Metodos
Volumen()
-------------
"""

pi=3.141592
class Cilindro():
    def superficie(radio,altura):
        area=(2*pi*float (radio)*float(altura)) + (2*pi*float(radio)**2)
        return area

    def volumen(pi, radio, altura):
        volumen=(pi*float(radio)**2)*float(altura)
        return volumen

    print (superficie(4,12))
    print(volumen(pi,4,12))
    


