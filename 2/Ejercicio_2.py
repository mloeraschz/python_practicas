import os
from os import getcwd ### Antes que nada, debemos importar la biblioteca "os".
from os import listdir ### Y también algunos métodos dentro de la biblioteca.
from os.path import isfile, join

dire = getcwd()
files = [f for f in listdir(dire) if isfile(join(dire,f)) and f[-3::] == 'CSV']

with open('NL.csv','w',encoding='utf-8' ) as archivo:
    archivo.write(u'\ufeff')
with open('DF.csv','w',encoding='utf-8' ) as archivo:
    archivo.write(u'\ufeff')
with open('JL.csv','w',encoding='utf-8' ) as archivo:
    archivo.write(u'\ufeff')

for file in files:
   
    with open(file,'r',encoding='utf-8') as archivo:
        texto = archivo.readlines()
    for linea in texto:
        try:
            lista2 = linea.split(',')
            #print(lista2)
            if 'Nuevo León'  in lista2[1]:
                with open('NL.csv','a',encoding='utf-8' ) as archivo:
                    archivo.write(texto[5])
                    archivo.write(linea)
            elif 'Jalisco'  in lista2[1]:
                with open('JL.csv','a',encoding='utf-8' ) as archivo:
                    archivo.write(texto[5])
                    archivo.write(linea)
            elif 'Distrito Federal' in lista2[1]:
                with open('DF.csv','a',encoding='utf-8' ) as archivo:
                    archivo.write(texto[5])
                    archivo.write(linea)
        except IndexError:
            pass
