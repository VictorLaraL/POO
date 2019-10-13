# Polimorfismo

La palabra "polimorfismo" del griego "poly" y "morphos" ("varias" y "formas") se refiere a la habilidad de objetos de distintas clases de responder al mismo mensaje. Esto se puede conseguir a través de la herencia: un objeto de una clase derivada es al mismo tiempo un objeto de la clase padre, de forma que allí donde se requiere un objeto de la clase padre, también se puede utilizar uno de la clase hija.
 
En ocaciones también se utiliza el término poliformismo para referirse a la sobrecarga de métodos, término que se define como la capacidad del lenguaje de determinar qué metodo ejecutar entre varios métodos con igual nombre según el tipo o numero de los parámetros que se le pasan.

```python
    class Persona:
        def __init__(self):
            self.cedula = 13765890
        def mensaje(self):
            print("mensaje desde la clase Persona")

    class Obrero(Persona):
        def __init__(self):
            self.__especialista = 1
        def mensaje(self):
            print("mensaje desde la clase Obrero")          
```

[Siguiente: Encapsulacion](Encapsulacion/Encapsulacion.md)