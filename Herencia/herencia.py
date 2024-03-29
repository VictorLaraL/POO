# --------------- Herencia simple ------------------
class Persona():
    # Clase que representa una Persona

    def __init__(self, cedula, nombre, apellido, sexo):
        # Constructor de clase Persona
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        # Devuelve una cadena representativa de Persona
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre, 
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        # Mostrar mensaje de saludo de Persona
        return mensaje

    def getGenero(self, sexo):
        # Mostrar el genero de la Persona
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"

class Supervisor(Persona):
    # Clase que representa a un Supervisor

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        # Constructor de clase Supervisor

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        # Devuelve una cadena representativa al Supervisor
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        # Mostrar las tareas del Supervisor
        return ', ', self.tareas             

# --------------- Herencia Multiple ------------------

class Destreza(object):
    # Clase la cual representa la Destreza de la Persona

    def __init__(self, area, herramienta, experiencia):
        # Constructor de clase Destreza
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia

    def __str__(self):
        # Devuelve una cadena representativa de la Destreza
        return """Destreza en el área %s con la herramienta %s, 
        tiene %s años de experiencia.""" % (
            str(self.area), self.experiencia, self.herramienta)


class JefeCuadrilla(Supervisor, Destreza):
    # Clase la cual representa al Jefe de Cuadrilla

    def __init__(self, cedula, nombre, apellido, sexo, 
        rol, area, herramienta, experiencia, cuadrilla):
        """Constructor de clase Jefe de Cuadrilla"""

        # Invoca al constructor de clase Supervisor
        Supervisor.__init__(self, cedula, nombre, apellido, sexo, 
            rol)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)

        # Nuevos atributos
        self.cuadrilla = cuadrilla

    def __str__(self):
        # Devuelve cadena representativa al Jefe de Cuadrilla"""
        jq = "{0}: {1} {2}, rol '{3}', tareas {4}, cuadrilla: {5}"
        return jq.format(
            self.__doc__[28:46], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas(), self.cuadrilla)

if __name__ == '__main__':
    pass