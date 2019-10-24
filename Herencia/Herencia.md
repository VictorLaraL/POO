# Herencia
 
El concepto de herencia en POO, es una abstracción del mundo para referirnos a cuando una clase hereda atributos y métodos de otra, es decir, que de una super clase heredemos los métodos y atributos a una subclase. También se le puede conocer a esta acción como extender de una clase.

Un ejemplo práctico para este concepto es el siguiente:

```python
    class Instrumento:
        def __init__(self, precio):
            self.precio = precio
            imprimir_precio()

        def imprimir_precio(self):
            print(‘El precio del instrumento es: {} pesos’.format(self.precio))

    class Guitarra(Instrumento):
        pass

    class Batería(Instrumento):
        pass
```

En el ejemplo anterior podemos ver cómo la clase instrumento tiene un atributo (precio) y un método (imprimir_precio), este atributo y método se podrán utilizar de igual forma en las clases 'Guitarra' y 'Batería', es decir, ahora los objetos de estas clases tendrán el atributo precio y el método imprimir_precio.

Ahora bien que pasaría si ambas clases ( Guitarra , Bateria), desearan tener su propio método __init__, bastaría con escribir un nuevo método tal y como lo haríamos normalmente, a esta acción se le conoce como sobreescritura de metodos. Otra situación que nos puede ocurrir es necesitar sobreescribir un método pero también el método de la clase padre, en este caso usaríamos la sintaxis SuperClase.metodo(self. args), para llamar al método de igual nombre de la clase padre. Por ejemplo, para llamar al método init de la clase padre de 'Guitarra' lo haríamos de la siguiente forma: Instrumento.__init__(self, precio).

# Herencia múltiple

En python a diferencia de otros lenguajes, se permite la herencia múltiple. Es decir, una clase puede heredar de varias clases a de manera simultánea. En el ejemplo anterior si almacenáramos los artículos musicales dentro de una tienda también podríamos crear una clase 'artículos', entonces 'Guitarra' y 'Batería' serian también artículos por lo que podrían heredar de ambas clases. p.ej.

```python
    class Guitarra(Producto, Instrumento)
        pass

    class Batería(Producto, Instrumento)
        pass
```

Entonces cuando generamos herencia múltiple puede ocurrir que las dos clases padre tengan un mismo método y en este caso se sobreescribirian pero siempre empezando por el método de la clase declarada más a la izquierda.

[codigo](/Herencia/herencia.py)

# Metodo super()

Esta función nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria) sin tener que nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria) cuando queramos y aún así mantener un código funcional, sencillo  y mantenible.

```python
class Perros(object): #Declaramos la clase principal Perros
    def ladrar (self):
        print ("""GUAAAUU GUAAAUU!""")

    def grunir (self):
        print ("""GRRRRRR GRRRRR""")

class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""guau guau guau""")

    def grunir(self):
        print ("""gññññiii gñññiiii""")

class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""GuaUUU GUAAAUUU GuaUUU""")

    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")

class Shepadoodle (Caniche, Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()

Tommy = Pastor_Aleman()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
                    #Y  si borramos ambos? Imprimirá el ladrido de Perros!
```

[Siguiente: Polimorfismo](/Polimorfismo/Polimorfismo.md)