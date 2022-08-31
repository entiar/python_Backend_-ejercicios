class Vehiculo:
    def __init__(self, color, ruedasv, puerta):
        self.color = color
        self.ruedasv = ruedasv
        self.puerta = puerta
    
class Coche(Vehiculo):
    def __init__(self, color, ruedasv, puerta, velocidad, cilindrada):
        self.color = color
        self.ruedasv = ruedasv
        self.puerta = puerta
        self.velocidad = velocidad
        self.cilindrada =  cilindrada
        

coche = Coche("azul", 4, 4, 150, 1200)
