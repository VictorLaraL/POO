# POO

## Introduccion
La programación orientada a objetos es un paradigma más de la programación que nos ayuda a modelar problemas de una manera que nos facilita la resolución de problemas o necesidades gracias a sus atributos, a continuación explicaremos los conceptos principales de este paradigma pero específicamente cómo hacerlo mediante el LP python.

## Objetos y Clases
Dentro del POO podemos hacer una abstracción del mundo real mediante lo que se conocen como objetos y clases. De ahora en adelante si utilizamos este paradigma nuestros programas entonces se basaran en estos dos tipos y sus interacciones entre estos dos mismos.

###    Objeto 
Es una entidad que agrupa un estado y una funcionalidad relacionadas. El estado del objeto se define a través de variables que llamamos atributos, mientras que la funcionalidad se modela a través de funciones a las que se les conoce con el nombre de métodos del objeto.  

###    Clase
Una clase no es más que una plantilla genérica a partir de la cual instanciar los objetos; plantilla que es la que define que atributos y métodos tendrán los objetos de esa clase.

###    Declaración en python
En python las clases se definen mediante la palabra clave 'class' seguido del nombre de la clase, dos puntos y a continuación, indentado respecto  al cuerpo de la clase.
 
    class Nombre_clase: #como BP usamos el nombre con su inicial en mayúscula

        def __init__(self):
            pass

        def fun(self):
            pass


El primer método, el cual declaramos tiene una característica en particular y es el uso de “__” al inicio y fin de la palabra "init". 
En python los métodos especiales tienen esta misma característica pero con nombres distintos (p.ej.  “__str__”, “__add__”, “__sub__”).

Pero en particular el método init nos sirve como constructor, es decir, que de acuerdo a los parámetros que nos pida el método en la clase, son los parámetros que ingresaremos al crear un objeto de dicha clase. Ejemplo:

    class Nombre_clase:

        def __init__(self, a, b):
            self.a = a
            self.b = b

    x = 5
    y = 10

    objeto = Nombre_clase(x, y)


Ahora bien, dentro de la declaración de nuestro constructor tenemos tres parámetros y nosotros solo le estamos pasando dos, esto es por que el primer parámetro hace referencia a que pertenece a la clase, y esta característica se aplica en todos los métodos a declarar (el nombre del primer parámetro puede ser cualquiera pero por BP se utiliza la palabra "self").

En el ejemplo anterior vemos que dentro del constructor tenemos declaradas dos variables a las que les asignamos los parámetros que recibimos, esto es por que la palabra "self" seguida del operador “ . “ nos sirve para especificar a una variable local dentro del objeto, es decir, cada vez que hagamos uso de esta tenemos que especificarla tal y como lo hacemos en el constructor.

## Herencia 
 
El concepto de herencia en POO, es una abstracción del mundo para referirnos a cuando una clase hereda atributos y métodos de otra, es decir, que de una super clase heredemos los métodos y atributos a una subclase. También se le puede conocer a esta acción como extender de una clase.

Un ejemplo práctico para este concepto es el siguiente:

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
    
En el ejemplo anterior podemos ver cómo la clase instrumento tiene un atributo (precio) y un método (imprimir_precio), este atributo y método se podrán utilizar de igual forma en las clases 'Guitarra' y 'Batería', es decir, ahora los objetos de estas clases tendrán el atributo precio y el método imprimir_precio.

Ahora bien que pasaría si ambas clases ( Guitarra , Bateria), desearan tener su propio método __init__, bastaría con escribir un nuevo método tal y como lo haríamos normalmente, a esta acción se le conoce como sobreescritura de metodos. Otra situación que nos puede ocurrir es necesitar sobreescribir un método pero también el método de la clase padre, en este caso usaríamos la sintaxis SuperClase.metodo(self. args), para llamar al método de igual nombre de la clase padre. Por ejemplo, para llamar al método init de la clase padre de 'Guitarra' lo haríamos de la siguiente forma: Instrumento.__init__(self, precio).

## Herencia múltiple

En python a diferencia de otros lenguajes, se permite la herencia múltiple. Es decir, una clase puede heredar de varias clases a de manera simultánea. En el ejemplo anterior si almacenáramos los artículos musicales dentro de una tienda también podríamos crear una clase 'artículos', entonces 'Guitarra' y 'Batería' serian también artículos por lo que podrían heredar de ambas clases. p.ej.

    class Guitarra(Producto, Instrumento)
        pass

    class Batería(Producto, Instrumento)
        pass

Entonces cuando generamos herencia múltiple puede ocurrir que las dos clases padre tengan un mismo método y en este caso se sobreescribirian pero siempre empezando por el método de la clase declarada más a la izquierda.

## Polimorfismo

La palabra "polimorfismo" del griego "poly" y "morphos" ("varias" y "formas") se refiere a la habilidad de objetos de distintas clases de responder al mismo mensaje. Esto se puede conseguir a través de la herencia: un objeto de una clase derivada es al mismo tiempo un objeto de la clase padre, de forma que allí donde se requiere un objeto de la clase padre, también se puede utilizar uno de la clase hija.

En ocaciones también se utiliza el término poliformismo para referirse a la sobrecarga de métodos, término que se define como la capacidad del lenguaje de determinar qué metodo ejecutar entre varios métodos con igual nombre según el tipo o numero de los parámetros que se le pasan.
 
## Encapsulacion

La encapsularon se refiere a impedir el acceso a determinados métodos y atributos de los objetos, estableciendo así que puede utilizarse desde fuera de la clase. En otros lenguajes de programación esto se consigue con los modificadores de acceso que definen si cualquiera puede acceder a esa función o variable (public) o si esta restringido el acceso a la propia clase (private).

En python no existen los modificadores de acceso, y lo que se suele hacer es que el acceso a una variable o funciona viene determinado por su nombre: si el nombre comienza con dos guiones bajos (pero no termina con dos guiones bajos), se trata de una variable o funcional privada, en caso contrario es publica.

Ejemplificando:

En ocasiones también puede suceder que queramos permitir el acceso a algún atributo de nuestro objeto pero de manera controlada, para esto podemos hacer uso de los famosos métodos 'get' y 'set' (getVariable, setVariable), nombre que reciben por conveniencia, pero que pueden recibir el nombre que queramos. 

Ejemplo:

## Metodos especiales

