"""Ejercicio 3Permalink
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima 
y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la 
temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de
 días que se van a introducir."""

#temperatura media de un día 
#temperatura máxima y mínima

def temperatura(temp_max, temp_min):
    temp_media=(temp_max+temp_min)/2
    return temp_media

temperatura(30,10)

dias=int(input("Cuantos dias quieres ingresar la temperatura?"))
for i in range(dias):
    temperaMax=float(input("Introduce la temperatura maxima: "))
    temperaMin=float(input("Introduce la temperatura minima: "))
    print("La temperatura promedio de este dia es: ", temperatura(temperaMax, temperaMin))
 
        
    


    

