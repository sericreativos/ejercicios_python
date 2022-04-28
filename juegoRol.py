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
    def __init__(self, vida:int, posicion:int, velocidad:int):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad
                   
# los métodos
#recibir_ataque, que reduzca la vida según una cantidad recibida y
#lance una excepción si la vida pasa a ser menor o igual que cero
    def recibir_ataque (self, vida:int, recibirAtaque:int):
        try:
            self.vida=vida
            self.vida -= recibirAtaque
        except:
            if self.vida < 0:
                self.vida=0
                print("You loose!!")
   

#y mover que reciba una dirección 
#y se mueva en esa dirección la cantidad indicada por velocidad.
    def mover_direccion (self, direccion:str, velocidad:int ):
        self.direccion=direccion
        direccion='derecha'
        self.velocidad=velocidad
        velocidad=9




#Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método 
#atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.

class soldado:
    def __init__ (self, vida:int, posicion:int, velocidad:int, ataque:int, cantidadAtaque:int):
        super(personaje).__init__(self, vida, posicion, velocidad, ataque)
        
    def atacar(personaje2, self, vida, cantidadAtaque): 
        self.vida -= vida
        vida -= cantidadAtaque
        
#Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método 
#cosechar, que devuelva la cantidad cosechada.
class campesino:
    def __init__(self,vida:int, posicion:int, velocidad:int, cosecha: int, cantidadCosechada:int):
        super(personaje).__init__(self, vida, posicion, velocidad, cosecha)

    def cosechar(self, cosecha,cantidadCosechada):
        self.cosecha= cosecha
        for i in range(cosecha):
            if cosecha > 1:
                cantidadCosechada += 1





        
