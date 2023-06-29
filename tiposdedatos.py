# datos de tipo numerico
edad = 18
peso = 98
estatura = 1.68
print(f"mi peso es de {peso}")

# operaciones aritmeticas basicas
imc = peso / (estatura**2)
print("Mi imc es de:",imc," \n")
print(type(imc))
print("Mi imc es de: {:.2f}".format(imc),"\n")

#datos de tipo cadena de caracteres
asignatura = "programacion"
carrera = "ingenieria civil en informatica"
print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)
print("la cantidad de caracteres de la palabra", carrera, "es de:",len(carrera))

#valores booleanos
ampolleta = False
interruptor = True
print(ampolleta,interruptor)
print("la variable ampolleta es de tipo:",type(interruptor),"\n")

#podemos transformar cualquier valor a un booleano
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))

#datos de tipo list
#inicializando listas de 2 maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia:",nueva_lista)
print("esta es otro lista vacia:",otra_lista)
print(type(otra_lista))

#declarando tres listas diferentes
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["JavaScript"]

#¿ se puede realizar una lista de datos compuestos?
data = ['Osorno', {'UV': 'NIVEL BAJO', 'temp "c': 15}, (-40.5725, -73.1353)]
listamixta = ['Nicolas', 50, True]
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de un elemento:",lenguaje)
print("esta es una lista mixta:",listamixta)
print("esto igual es una lista:",data)
print(len(listamixta))
print(estudiantes.count("pepe"))
print(num.count(5000))

lenjuaje = ["JavaScript"]
print("nuevo valor del Arreglo de un elemento:",lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print(estudiantes[0])
print(estudiantes[1])
print("posicion -2",estudiantes[-2])

#sumar listas
print("suma de litas",estudiantes + num)
print(list(range(1,5)))
print("\n")

#tuplas-(no mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print(type(grupo1))
print("indice del elemento:",grupo1.index ("Daniel"))
grupo2 = ("pedro",100,"felipe","diego",2020,"alejandra")
print("trozo de la tupla",grupo2[0:3])

#sets "conjuntos"
conjunto_vacio = set()
conjunto_vacio1 = {}
print(type(conjunto_vacio1))
conjunto_colores = set({"azul","rojo","verde"})
conjunto_animales = set({"perro","gato"})

conjunto_colores.add("celeste")
print("el set de colores lo conforman:",conjunto_colores)
#list = []
#tp = ()
#st = {}
#di = {}
conjunto_colores_1 = set({"rojo","naranjo","verde"})
conjunto_animales_2 = ({"caballo","vaca","oveja"})
print("el set de colores se conforman por",conjunto_colores_1)

diccionario1 = dict()
diccionario2 = {}
datos_personales = {
    "nombre":"nicolas",
    "institucion":"ulagos",
    "edad":19,
    "ciudad":"la union"
}
print("diccionario inicial:",datos_personales)