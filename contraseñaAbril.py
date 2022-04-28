"""1.Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la 
contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

2.Modificar el programa anterior para que solamente permita una cantidad fija de inten-tos."""
intentos=0
contraseña=''
contraAlmacenada= "pokemon"


while intentos < int(3):    
    contraseña= input (str("Ingresa tu contraseña: "))
    if contraseña!=contraAlmacenada:
        intentos += 1
            
    else:
        print("Bienvenido ")
        break

print("Has excedido el numero de intentos")

