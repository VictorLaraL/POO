import math

class Punto():
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

class Poligono():
    def __init__(self, numLados):
        self.numLados = numLados

    def area(self, *puntos):
        if(len(puntos) == 3):
            triangulo = Triangulo()
            triangulo.area()

        elif(len(puntos) == 4):
            cuadrado = Cuadrado()
            cuadrado.area()

        elif(len(puntos) >= 5):
            pass
        else:
            print('No cuentas con los puntos necesarios!')

    def distDosPuntos(p1, p2):
        distancia = math.sqrt((p2.getX() - p1.getX()) + (p2.getY() - p1.getY()))
        return distancia

    def __str__(self):
        return ''' 
        Los puntos del triangulo son: {}, {}, {},
        El area es: {}
        El perimetro es: {}
        '''

class Triangulo(Poligono):
    def __init__(self):
        

    def __str__(self):
        return ''' 
        Los puntos del triangulo son: {}, {}, {},
        El area es: {}
        El perimetro es: {}
        '''

class Cuadrado(Poligono):
    

    def __str__(self):
        return ''' 
        Los puntos del triangulo son: {}, {}, {},
        El area es: {}
        El perimetro es: {}
        '''

if __name__ == "__main__":
    
    print('''---------------------------------
                Calculadora de poligonos
                1) ingresar puntos
                2) Calcular
    ''')



