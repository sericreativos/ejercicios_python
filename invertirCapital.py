"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

def inversion(capital, interes,años):
    capital=(float (input("Introduce la cantidad a invertir: "))) 
    interes=(float (input("Introduce el interes anual que quieres obtener: ")))
    años=(float (input("A cuantos años quieres invertir: ")))

    total=(capital+interes)*años

    print("El total de tu inversion es: ", total, "en ", años, "años")

    return total
inversion(5000,500,1)