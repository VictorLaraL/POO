# https://www.evernote.com/l/AkA_cyWY_HpOZIChdB8S3dgfHoBE-8hJBJs/

import math

class Punto():
    # Clase que genera los puntos en el plano
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # ----- Metodos get -----
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    # ----- Metodos set -----
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __str__(self):
        return 'x = {}, y = {}'.format(self.__x, self.__y)

class PoligonoR():
    # Clase que recibe una lista de puntos y calcula el area y perimetro de las figuras
    def __init__(self, puntos):
        self.puntos = puntos
        
    def area(self):
        # Calculamos el area del poligono dependiendo del numero de puntos que tenga
        if(len(self.puntos) == 3 and self.comprobacionPI()):
            triangulo = Triangulo(self.puntos)
            return triangulo.area()       
        elif(len(self.puntos) == 4 and self.comprobacionPI()):
            cuadrado = Cuadrado(self.puntos)
            return cuadrado.area()
        elif(len(self.puntos) >= 5 and self.comprobacionPI()):
            return self.areaPolReg()
        else:
            print('No cuentas con los puntos necesarios!')

    def areaPolReg(self):
        # Calculamos el area de poligonos regulares de 5 o mas lados
        cantPunt = len(self.puntos)

        # Calculo del area de un poligono regular de cantidad de puntos pares
        if (cantPunt % 2 == 0): 
            apotema = (self.distDosPuntos(self.puntoMedio(self.puntos[0], self.puntos[1]), (self.puntoMedio(self.puntos[cantPunt/2], self.puntos[(cantPunt/2)+1]))))/2
            areaP = (self.perimetro() * apotema)/2
            return areaP    
        else:
            # Calcular area del poligono regular de lados impares
            pass

    def perimetro(self):
        perimetro = 0
        for x in range(1,len(self.puntos)):
            perimetro += self.distDosPuntos(self.puntos[x-1], self.puntos[x])
        return perimetro

    def comprobacionPI(self):
        # Comprobamos que sea un Poligono y que sea regular 
        dist1 = self.distDosPuntos(self.puntos[0], self.puntos[1])
        dist2 = self.distDosPuntos(self.puntos[1], self.puntos[2])

        # Comprobacion de que es un poligono puesto que el primer punto se une con el ultimo 
        if (dist1 == self.distDosPuntos(self.puntos[0], self.puntos[len(self.puntos)-1])): 
            for x in range(3,len(self.puntos)):
                # Comprobacion entre las aristas de la figura
                if (dist1 != dist2): 
                    return False
                dist1 = dist2
                dist2 = self.distDosPuntos(self.puntos[x-1], self.puntos[x])            
            return True
        else:
            return False

    def distDosPuntos(self, p1, p2):
        # Calculamos la distancia entre dos puntos
        distancia = math.sqrt(((p2.getX() - p1.getX())**2) + ((p2.getY() - p1.getY())**2))
        return distancia

    def puntoMedio(self, p1, p2):
        # Calculamos el punto medio entre dos puntos
        x = (p1.getX() - p2.getX())/2
        y = (p1.getY() - p2.getY())/2
        return Punto(x,y)

    def imprimirPuntos(self):
        # Imprimimos los puntos en un objeto Poligono
        for punto in self.puntos:
            print(punto)
        return 'Son los puntos del Poligono'

    def __str__(self):
        return '{}'.format(self.imprimirPuntos())

class Triangulo(PoligonoR):
    # Clase que hereda de PoligonoR y calcula el area de un triangulo regular
    def __init__(self, puntos):
        super().__init__(puntos)

    def area(self):
        altura = super().distDosPuntos(super().puntoMedio(self.puntos[0], self.puntos[1]), self.puntos[2])
        base = super().distDosPuntos(self.puntos[0], self.puntos[1]) 
        areaT = (base * altura)/2
        return areaT 
        
class Cuadrado(PoligonoR):
    # Clase que hereda de PoligonoR y calcula el area de un cuadrado (poligono reg de 4 lados)
    def __init__(self, puntos):
        super().__init__(puntos)

    def area(self):
        areaC = super().distDosPuntos(self.puntos[0], self.puntos[1]) * super().distDosPuntos(self.puntos[1], self.puntos[2])
        return areaC  
    
if __name__ == "__main__":

    listaC = [Punto(1,1), Punto(-1,1), Punto(-1,-1), Punto(1,-1)]
    cuad = Cuadrado(listaC)
    polig = PoligonoR(listaC)

    print(polig)

    print(cuad)

    print(polig.area())

    print(polig.perimetro())