import os
from os import getcwd ### Antes que nada, debemos importar la biblioteca "os".
from os import listdir ### Y también algunos métodos dentro de la biblioteca.
from os.path import isfile, join

dire = getcwd()
files = [f for f in listdir(dire) if isfile(join(dire,f)) and f[-3::] == 'CSV']

with open('output.csv','w',encoding='utf-8' ) as archivo:
    archivo.write(u'\ufeff')

for file in files:
   
    with open(file,'r',encoding='utf-8') as archivo:
        texto = archivo.readlines()
    for linea in texto:
        if 'Nuevo León' in linea:
            with open('output.csv','a',encoding='utf-8' ) as archivo:
                archivo.write(texto[5])
                archivo.write(linea)
                
                
                
        
