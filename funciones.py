#declarando la primera funcion
def mi_primera_funcion():
    print("Esta es mi primera funcion")

mi_primera_funcion()

#declarando una funcion y utilizando listas
def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]
#concatenar()
print(concatenar(lista1,lista2))

#declarando una funcion multiplicacion pasando parametro
def multiplicacion (num1,num2):
    return num1*num2

#multiplicacion()
print(multiplicacion(10,2))

#ejemplo de una funcion
def suma(a, b):
    return a + b 

def resta(a, b):
    return a - b 

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
#se llama a la funcion suma
resultado = suma(a, b)
print("La suma es de:",resultado)
# se llama a la funcion resta
resultado2 = resta(a, b)
print("La resta es de:",resultado2)