"""En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola."""

class Vehiculo:
    def __init__(self, color, ruedasv, puerta):
        self.color = color
        self.ruedasv = ruedasv
        self.puerta = puerta
    
class Coche(Vehiculo):
    velocidad = 2
    cilindrada = 10000

co = Vehiculo("green", 4, 6)
co.Coche.velocidad()
