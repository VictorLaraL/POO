# Ejemplo de abstraccion para el paradigma POO

class Auto: # Como BPP la primer letra del nombre va en mayusulas
    def __init__(self, marca, gasolina):
        self.marca = marca
        if (gasolina > 0):
            self.gasolina = gasolina*2
            self.encender_auto()
        else:
            self.gasolina = gasolina
            self.gasolina = 2

    def encender_auto(self):
        if self.gasolina > 0:
            print('El auto se a encendido y tiene: {} litros de gasolina'.format(self.gasolina))
        else:
            print('Lo sentimos no tiene gasolina su auto')

    def acelerar(self):
        print('avanzamos 1 km')
        self.gasolina -= 1
        
    def frenar(self):
        print('El auto marca {} se ah detenido'.format(self.marca))

    def __str__(self):
        return 'el auto {} tiene {} litros de gasolina'.format(self.marca, self.gasolina)
        
if __name__ == '__main__':
    
    lista_autos = []

    while True:
        marca = input('ingresa la marca del auto: \n>')
        if marca == 'x':
            break
        gasolina = int(input('ingresa la cantidad de gasolina: \n>'))
        auto = Auto(marca, gasolina)
        lista_autos.append(auto)

    for auto in lista_autos:
        print(auto)