"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase 
llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir 
los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con 
el resultado de la nota y si ha aprobado o no.
"""
class Alumnos:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def metodo(self):
        if self.nota > 50:
            print("El alumno ", self.nombre, "aprobo el curso con: ", self.nota )
        else:
            print("El alumno ", self.nombre, "reprobo el curso con: ", self.nota)
p1 = Alumnos("nestor", 33)
p1.metodo()
