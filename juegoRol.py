"""Ejercicio 15.5.2. Juego de Rol

Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos
recibir_ataque, que reduzca la vida según una cantidad recibida y

lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección 
y se mueva en esa dirección la cantidad indicada por velocidad.

Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método 
atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método 
cosechar, que devuelva la cantidad cosechada."""

#Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad,
class personaje:
    def __init__(self,vida:int, posicion:int, velocidad:int):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad
                   
# los métodos
#recibir_ataque, que reduzca la vida según una cantidad recibida y
#lance una excepción si la vida pasa a ser menor o igual que cero
    def recibir_ataque (self, vida:int, recibirAtaque:int, vidaActual:int):
        self.recibirAtaque= recibirAtaque
        self.vida= vida
        self.vidaActual=vidaActual
        
        if int (recibirAtaque) > 1:
                vidaActual=vida-int (recibirAtaque)
                vidaActual -= 1            
                print(vidaActual)

        
        else:
            print("Perdiste")
               
    recibir_ataque(0,3,5,8)

#y mover que reciba una dirección 
#y se mueva en esa dirección la cantidad indicada por velocidad.
    def mover_direccion (direccion:int, velocidad:int ):
        if velocidad>1:
            direccion += 3
            direccionActual=direccion
        return direccionActual
                
    mover_direccion(2,8)

                    
#Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método 
#atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.

class soldado:
    def __init__ (vida:int, posicion:int, velocidad:int, ataque:int, lanzaAtaque:int):
        super(personaje).__init__(vida, posicion, velocidad, ataque)
        
    def atacar(personaje, vida, cantidadAtaque, lanzaAtaque): 
                if lanzaAtaque > 1:
                    cantidadAtaque >= 2
                    cantidadAtaque >= 5
                    vidaActual=vida-recibirAtaque
                    vidaActual += vidaActual 


        
#Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método 
#cosechar, que devuelva la cantidad cosechada.
class campesino():
    def __init__(self,vida:int, posicion:int, velocidad:int, cosecha: int, cantidadCosechada:int):
        super(personaje).__init__(self, vida, posicion, velocidad, cosecha)

    def cosechar(cosecha,cantidadCosechada):
        for i in range(cosecha):
            if cosecha > 1:
                cantidadCosechada += 1
        print(cantidadCosechada)


        
        
