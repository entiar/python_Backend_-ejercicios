#Escribe una función que calcule el área de un triángulo, recibiendo la 
#altura y la base como parámetros y otra función que calcule el área de un 
#círculo recibiendo el radio del mismo.
def areaTri(a, b):
    return (a*b)/2

def areaCir(r):
    pi = 3.1416
    return pi * (r **2)

print(areaTri(2,3))
print(areaCir(4))
