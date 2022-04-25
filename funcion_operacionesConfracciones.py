"""Ejercicio 13Permalink
Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a 
utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

**Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando 
leas una fracción debes simplificarla.
**Escribir_fracción: Esta función escribe en pantalla la fracción. Si el denominador es 1, se muestra 
sólo el numerador.

**Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.

Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y 
denominador por el MCD del numerador y denominador.

Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos
 fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y
  denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2.
 Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello
 numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello 
numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.

Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
Salir """

#Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando 
#leas una fracción debes simplificarla.
def leer_funcion (numerador,denominador,n):#8/32 4/16 2/8 1/4
    simplificada=int(numerador)/n, int(denominador)/n
    return simplificada
    
leer_funcion(8, 12, 2)

#Escribir_fracción: Esta función escribe en pantalla la fracción. Si el denominador es 1, se muestra 
#sólo el numerador.
def escribir_funcion (numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(numerador, "/", denominador )

escribir_funcion(16, 1)

#Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
def calcular_mcd (n1, n2):
    
        resto=n1%n2
        if resto==0:
            return n2 
        else:
            return calcular_mcd(n2, resto) 
calcular_mcd(16,4)

#Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y 
#denominador por el MCD del numerador y denominador.
def simplificar_fraccion (numerador, denominador):
    mcd=calcular_mcd(numerador, denominador)
    numerador=int (numerador)/mcd
    denominador=int (denominador)/mcd
    return numerador, denominador
simplificar_fraccion(24, 4)

#Sumar_fracciones: Función que recibe dos fracciones n1/d1 y n2/d2, y calcula la suma de las dos
#fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y
#denominador=d1*d2. Se debe simplificar la fracción resultado.

def sumar_fracciones(n1,n2,d1,d2):
    numerador=(n1*d2)+(d1*n2)
    denominador=d1*d2
    resultado=simplificar_fraccion(numerador, denominador)
    return resultado

sumar_fracciones(4,6,2,8)


#Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2.
#Se debe simplificar la fracción resultado.
def restar_fracciones(n1,n2,d1,d2):
    numerador=(n1*d2-d1*n2)
    denominador= d1*d2
    resultadoResta= simplificar_fraccion(numerador,denominador)
    return resultadoResta
restar_fracciones(4,6,2,8)

#Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello
#numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
def multiplicar_fracciones(n1,n2,d1,d2):
    numerador=n1*n2
    denominador=d1*d2
    resultadoMulti=simplificar_fraccion(numerador, denominador)
    return resultadoMulti

multiplicar_fracciones(4,6,2,8)

#Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello 
#numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.

def dividir_fracciones(n1,n2,d1,d2): 
    numerador=n1*d2
    denominador=d1*n2
    resultadoDivi=simplificar_fraccion(numerador, denominador)
    return resultadoDivi 

dividir_fracciones(4,6,2,8)





