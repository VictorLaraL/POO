# Encapsulación.

La encapsulación se refiere a impedir el acceso a determinados métodos y atributos de los objetos, estableciendo así, que puede utilizarse desde fuera de la clase. En otros lenguajes de programación esto se consigue con los modificadores de acceso que definen sí cualquiera puede acceder a esa función o variable (public) o sí esta restringido el acceso a la propia clase (private).

En python no existen los modificadores de acceso, y lo que se suele hacer es que el acceso a una variable o función viene determinado por su nombre: sí el nombre comienza con dos guiones bajos (pero no termina con dos guiones bajos), se trata de una variable o función privada, en caso contrario es pública.

```python
    class NombreClase:
        __atributo1
        __atributo2

    def __método1(self):
        pass

    def __método2(self):
        pass
```

Ejemplo de encapsulación:

```python
    class CajaSeguridad:
        __contraClave = '123qwe'

        def seguro(self, clave):
            if self.__contraClave == clave :
                print('Acceso concedido')
            else :
                print('Acceso denegado')
```

En ocasiones también puede suceder que queramos permitir el acceso a algún atributo de nuestro objeto, pero de manera controlada, para esto podemos hacer uso de los famosos métodos 'get' y 'set' (getVariable, setVariable), nombre que reciben por conveniencia, pero que pueden recibir el nombre que queramos.

```python
    class CajaSeguridad:
        __contraClave = '123qwe'

        def seguro(self, clave):
            if self.__contraClave == clave :
                print('Acceso concedido')
            else :
                print('Acceso denegado')

        def getClave(self):
            return self.__contraClave

        def setClave(self, nuevaClave):
            self.__contraClave = nuevaClave
```
