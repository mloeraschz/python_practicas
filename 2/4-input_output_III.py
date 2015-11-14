#### INPUT Y OUTPUT
#### Tercera parte: abriendo varios archivos con un mismo script

#### Por ahora ya debes saber cómo abrir y leer un archivo usando un script
#### de Python. Pero usualmente tenemos la tarea de explorar múltiples archivos
#### para encontrar la información que nos interesa. Para esto podriamos
#### especificar el nombre de cada archivo en una lista y usar un loop
#### for para abrirlo. ¿Pero no hay una manera más sencilla?
####
#### Sí la hay: usar la biblioteca "os".
####
#### La biblioteca "os", en general, contiene funciones y métodos para
#### hacer scripts que exploren la computadora local.
#### Entre las aplicaciones de la biblioteca "os" se encuentran
#### cambiar los nombres de los archivos del sistema y enlistar
#### las ubicaciones de todos los archivos y carpetas. Lo que nosotros
#### vamos a hacer es algo más simple: colocar todos los archivos que nos
#### interesan en una carpeta y acceder a todos los archivos de esa carpeta
#### usando la biblioteca "os".
####
#### 1. ENUMERANDO LOS ARCHIVOS 
####

import os ### Antes que nada, debemos importar la biblioteca "os".
from os import listdir ### Y también algunos métodos dentro de la biblioteca.
from os.path import isfile, join


dire = os.getcwd()  #### El método '.getcwd()' obtiene el directorio actual.
                    #### Es decir, el directorio donde está guardado el script,
                    #### que es donde también están nuestros archivos .csv
print(dire)

files = [f for f in listdir(dire) if isfile(join(dire,f)) and f[-3::] == 'CSV']
#### Aquí usamos list comprehension para crear una lista de solamente
#### los archivos presentes en un directorio. Para ello usamos las funciones:
#### listdir(directorio) <--- Enumera los archivos y carpetas de un directorio
#### isfile()            <--- Prueba (True or False) si un path es un archivo
####                          y no una carpeta.
#### join(directorio,archivo) <--- Une la dirección completa de un directorio
####                               con el nombre de un archivo para crear un
####                               path completo.
#### Si te fijas bien, también filtramos solamente los archivos con extensión
#### en CSV.

#### 2. LEYENDO CADA ARCHIVO

for x in files:
    print(join(dire,x))
    ar = open(join(dire,x),'r', encoding='utf-8')
    txt = ar.readlines()
    ar.close()
    
#### 3. FILTRANDO LOS DATOS
    
    for y in txt[:32]:
        linea = y.strip()
        linea = linea.replace('"','')
        linea = linea.split(',')
        
#### 4. SORTEANDO A LAS EXCEPCIONES Y HACIENDO UN ARCHIVO DE OUTPUT
        try:
            if linea[1] == 'Distrito Federal' or linea[1] == 'Nuevo León':
                with open('bambi.csv','a') as output:
                    output.write(','.join(linea))
                    output.close()
        except IndexError:
            pass

