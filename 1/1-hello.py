##### Este script va a imprimir la cadena de caracteres (string) "Hello world!"

print("Hello world!")

##### Las strings también pueden asociarse a variables.
##### Las variables pueden tener el nombre que queramos.

miVariable = "Hello world!"
print(miVariable)

##### Las variables pueden ser strings, números, listas, tuples y diccionarios.
##### Se pueden hacer diferentes operaciones con esas variables.
##### Empezemos por los strings.
##############################
##############################
##### Operaciones básicas con strings

miString = "Dinosaurio"

##### Vamos a añadir más texto

miString += " verde"

##### Vamos a obtener el primer y último caracter de nuestro string

print(miString[1])
print(miString[-1])

##### Vamos a obtener la longitud de nuestra string

print(len(miString))

##### Vamos a obtener el subtexto que va del 2do al 6to caracter del string

print(miString[1:7:])

##### Ahora el subtexto que va del 6to caracter al último

print(miString[6:-1:])

##### Los strings pueden escribirse de diferentes maneras

soyString = "Hola"

yoTambien = 'Hola, otra vez'

yYoTambien = '''Hola de nuevo,
¿ves cómo ahora puedo cambiar de línea
usando los tres apóstrofes?'''

##### Algunos métodos útiles con strings son:

miString = "Hola, soy una string de varias palabras"
miString = miString.upper()        ### Transformar a mayúsculas
print(miString)
miString = miString.lower()        ### Transformar en minúsculas
print(miString)
miString = miString.replace('string','cadena de caracteres')
print(miString)                     ### Sustituir una sub-string
miString = miString.split(" ")      ### Dividir la string cada espacio
print(miString)                     ### y transformar a lista.


