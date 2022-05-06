"""La unidad de patrimonio historico requiere registrar los siguientes datos: cantidad de cuartos,
 puertas y ventanas de aquellos inmuebles de color blanco, ademas de su superficie en mt2. 
 Para ello se solicita crear un programa que contenga la definicion de la clase Micasa y la 
 creacion de un objeto que calcule:
    -El precio total de la vivienda a un precio comercial de $450 el m2 construido y $280 el m2 sin
    construir
    -El tamaño final de la superficie del inmueble si se realiza una expansion del 50%.
    -El tamaño final de la superfciie del inmueble si se realiza una reduccion del 35%
    
    La Clase, los atributos y metodos son:
    _____________________
    Micasa                  Clase
    _____________________
    Color                   Atributo(s)
    _____________________   de clase
    Cuartos                 
    Puertas                 Atributo(s)
    Ventanas                de instancia
    Superficie
    _____________________
    Precio()                Metodos
    Expansion()
    Reduccion()
    _____________________
        """


class Micasa():
    def calcular(cuartos,puertas,ventanas,superficie):
        calSuperficie=(int(cuartos)+int(puertas)+int(ventanas)+int(superficie))
        precioCons=int(450)#x mt2 contruido 
        precioSinC=int(280)#x mt2 sin construir
        
        precioTotalConstruido=(precioCons*calSuperficie)
        print("El precio total comercial de la vivienda es de: ",precioTotalConstruido)
        precioTotalSin=(precioSinC*calSuperficie)
        print("El precio total comercial de la vivienda sin Construir es de: ", precioTotalSin)
        porcentajeExpans=0.50
        porcentajeReducc=0.35
        TotalExpansionCons=(calSuperficie*porcentajeExpans)+calSuperficie
        print("El tamaño final de la superficie del inmueble si se realiza una expansion del 50%: ",TotalExpansionCons)
        TotalReducionCons=(calSuperficie*porcentajeReducc)+calSuperficie
        print("El tamaño final de la superficie del inmueble si se realiza una reduccion del 35%: ",TotalReducionCons)
        return precioTotalConstruido, precioTotalSin, TotalExpansionCons, TotalReducionCons


    calcular(3,5,6,150)
    




