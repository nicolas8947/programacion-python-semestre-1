#operaciones aritmeticas con flotantes
v = "g * t"

c1 = 4 + 3j
print(type(c1))
c2 = complex(3,-5)

#operadores de comparacion
print("a > b")

animal_domestico =  "gato"
animal_salvaje = "Leopardo"

print(animal_domestico == animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(len(animal_domestico ) == len(animal_salvaje))

bencina = True
encendido = False
edad = 19
if bencina and encendido: 
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

if not bencina or (encendido and edad >= 19):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")