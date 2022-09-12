"""En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los 
elementos impares de una lista pasada por parámetro con filter y realizará 
una suma de todos estos elementos obtenidos mediante reduce."""
lista = [4,3,2,5,7,8,9,22,14,46]
def mifuncion(x):
    if x % 2 != 0:
        return True
    return False
resultado = filter(mifuncion, lista)
print(list(resultado))
