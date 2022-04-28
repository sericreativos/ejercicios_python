"""Ejercicio 15.5.2. Juego de Rol

Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos
recibir_ataque, que reduzca la vida según una cantidad recibida y

lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección 
y se mueva en esa dirección la cantidad indicada por velocidad.

Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método 
atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método 
cosechar, que devuelva la cantidad cosechada."""


class personaje():
    def __init__(self, vida:int, posicion:int, velocidad:int):
        self.vida= vida
        print(self.vida)
        self.posicion = posicion
        print(self.posicion)
        self.velocidad = velocidad
        print(self.velocidad)


    def recibir_ataque (recibirAtaque, vidaMenos):
        try:
            recibirAtaque.vida=vidaMenos
            vidaActual=recibirAtaque-vidaMenos
            
        except:
            if vidaActual <= 0:
                print("You loose!!")

    def mover_direccion (moverDireccion, moverCantidad, posicion, velocidad ):
        moverDireccion.posicion=posicion
        print(moverDireccion.posicion)
        moverCantidad.velocidad=velocidad
        print(moverCantidad)

class soldado(personaje):
    def __init__ (self, vida:int, posicion:int, velocidad:int, ataque:int):
        personaje.__init__(self, vida, posicion, velocidad, ataque)

    def atacar(personaje_2):
        def __init__(ataque):
            soldado.__init__(ataque)
        
            

class campesino():
    def __init__(self,vida:int, posicion:int, velocidad:int, cosecha: int):
        personaje.__init__(self, vida, posicion, velocidad, cosecha)

    def cosechar(self, cosecha):
        self.cosecha= cosecha
        return cosecha

    





        
