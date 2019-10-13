# Encapsulacion

La encapsularon se refiere a impedir el acceso a determinados métodos y atributos de los objetos, estableciendo así que puede utilizarse desde fuera de la clase. En otros lenguajes de programación esto se consigue con los modificadores de acceso que definen si cualquiera puede acceder a esa función o variable (public) o si esta restringido el acceso a la propia clase (private).

En python no existen los modificadores de acceso, y lo que se suele hacer es que el acceso a una variable o funciona viene determinado por su nombre: si el nombre comienza con dos guiones bajos (pero no termina con dos guiones bajos), se trata de una variable o funcional privada, en caso contrario es publica.

```python
    class NombreClase:
        __atributo1
        __atributo2

    def __metodo1(self):
        pass

    def __metodo2(self):
        pass
```

Ejemplo de encapsulacion:

```python
    class CajaSeguridad:
        __contraClave = '123qwe'

        def seguro(self, clave):
            if self.__contraClave == clave :
                print('Acceso concedido')
            else :
                print('Acceso denegado')
```

En ocasiones también puede suceder que queramos permitir el acceso a algún atributo de nuestro objeto pero de manera controlada, para esto podemos hacer uso de los famosos métodos 'get' y 'set' (getVariable, setVariable), nombre que reciben por conveniencia, pero que pueden recibir el nombre que queramos. 

```python
    class CajaSeguridad:
        __contraClave = '123qwe'

        def seguro(self, clave):
            if self.__contraClave == clave :
                print('Acceso concedido')
            else :
                print('Acceso denegado')

        def getClave(self):
            return __contraClave

        def setClave(self, nuevaClave):
            __contraClave = nuevaClave
```