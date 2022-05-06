""" Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número
hasta cero separados por comas."""

def cuentaAtras(num):
    num=int(input("Introduce un numero entero positivo"))

    for i in range(num,-1,-1):
        print(i)
    return i

cuentaAtras(10)