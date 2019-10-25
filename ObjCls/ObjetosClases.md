# Objetos y Clases.
Dentro del POO podemos hacer una abstracción del mundo real mediante lo que se conocen como objetos y clases. De ahora en adelante, si utilizamos este paradigma, nuestros programas se basaran, entonces, en estos dos tipos y sus interacciones entre estos dos mismos.

## Objeto.
Es una entidad que agrupa un estado y una funcionalidad relacionadas. El estado del objeto se define a través de variables que llamamos atributos, mientras que, la funcionalidad se modela a través de funciones a las que se les conoce con el nombre de métodos del objeto.  

## Clase.
Una clase no es más que una plantilla genérica a partir de la cual instanciar los objetos; plantilla es la que define que atributos y métodos tendrán los objetos de esa clase.

![auto](/imgs/ObjCls.png)

## Declaración en python.
En python las clases se definen mediante la palabra clave 'class' seguido del nombre de la clase, dos puntos y a continuación, indentado respecto  al cuerpo de la clase.

```python
    class Nombre_clase: #como BP usamos el nombre con su inicial en mayúscula.

        def __init__(self):
            pass

        def fun(self):
            pass
```

El primer método, el cual declaramos, tiene una característica en particular y es el uso de “__” al inicio y final de la palabra "init". 
En python, los métodos especiales tienen esta misma característica, pero con nombres distintos (p.ej.  “__str__”, “__add__”, “__sub__”).

Pero en particular, el método init nos sirve como constructor, es decir, que de acuerdo a los parámetros que nos pida el método en la clase, son los parámetros que ingresaremos al crear un objeto de dicha clase. Ejemplo:

```python
    class Nombre_clase:

        def __init__(self, a, b):
            self.a = a
            self.b = b

    x = 5
    y = 10

    objeto = Nombre_clase(x, y)
```

Ahora bien, dentro de la declaración de nuestro constructor tenemos tres parámetros y nosotros solo le estamos pasando dos, esto es, porque el primer parámetro hace referencia a que pertenece a la clase, y esta característica se aplica en todos los métodos a declarar (el nombre del primer parámetro puede ser cualquiera, pero por BP se utiliza la palabra "self").

En el ejemplo anterior vemos que dentro del constructor tenemos declaradas dos variables a las que les asignamos los parámetros que recibimos, esto es, porque la palabra "self" seguida del operador “ . “ nos sirve para especificar a una variable local dentro del objeto, es decir, cada vez que hagamos uso de esta tenemos que especificarla tal y como lo hacemos en el constructor.

[codigo](/ObjCls/ejemploAuto.py)

[Siguiente: Metodos Especiales](/MetEsp/MetodosEspeciales.md)
