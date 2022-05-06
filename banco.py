"""problema 4
Un banco tiene 3 clientes que pueden hacer depositos y retiros. Simular estas operaciones. Asi 
mismo el banco requiere que al final del dia se calcule el saldo final de cada cliente.
Los atributos y metodos de clase son :
__________________
Cliente           |Clase
__________________|
Nombre            |Atributos 
Monto             |de
__________________|Instancia
Deposito (Monto)  |
Retiro(Monto)     |Metodos
ImprimirSaldo()   |
__________________|
"""

class Cliente():
    def banco(nombre,monto):
        nombre=""
        autorizados="Humberto","humberto","Luis","luis","zoe","Zoe"
        saldo=0

        nombre=input("Ingresa tu nombre: ")
        if nombre in autorizados:
            print("Bienvenido ", nombre)
            while True:
                if nombre in autorizados: 
                    menu=input("Que deseas hacer? 1)Deposito en efectivo 2)Retirar efectivo 3)Proporcionar saldo despues de tus operaciones 4)Terminar ")
                    if menu== str(1):
                        monto=float(input("Ingresa la cantidad a depositar: "))
                        if monto>0:
                            saldo += monto
                        else:
                            print("La cantidad no es valida")

                    if menu==str(2):
                        monto= float(input("Ingresa la cantidad a retirar: "))
                        if monto>saldo:
                            print("Estas excediendo la cantidad en tu cuenta ")
                        else:
                            saldo -= monto
                            
                    if menu==str(3):
                        print("Hola ",nombre,"Tu saldo de hoy es: ",saldo )
                    if menu==str(4):
                        print("Estas saliendo del sistema")
                        break
        else:
            print("Bienvenido usuario, no podras realizar todas las operaciones")
            menu=input("Que deseas hacer? 1)Deposito en efectivo  2)Proporcionar saldo despues de tus operaciones 3)Terminar ")
            if menu== str(1):
                monto=float(input("Ingresa la cantidad a depositar: "))
                if monto>0:
                    saldo += monto
                else:
                    print("La cantidad no es valida")
            if menu==str(2):
                print("Hola ",nombre,"Tu saldo de hoy es: ",saldo )
            if menu==str(3):
                print("Estas saliendo del sistema")
                
                

    banco("",1)



            
