## XML y BEAUTIFUL SOUP
##
## Los archivos XML permiten almacenar datos en una estructura jerárquica,
## utilizando tags. Sin embargo, a diferencia de los tags de HTML,
## los tags de XML podemos definirlos arbitrariamente y no tienen información
## acerca del formato para la presentación de los datos (color y tipo de fuente,
## encabezado, etc.)
##
## BeautifulSoup permite también interpretar este tipo de archivos. Vamos
## a utilizar como ejemplo el archivo XML que es típico de tu área de estudio,
## si no lo tienes, puedes utilizar un archivo de resultados de BLAST.


## 1. Importamos las bibliotecas requeridas
import urllib2
from bs4 import BeautifulSoup
import csv


## 2. Abrimos nuestro XML
archivo = open('59CHRTMZ01R-Alignment.xml','r')
texto = archivo.read()
archivo.close()
#print(texto)

## 3. Interpretamos el XML con BeautifulSoup
soup = BeautifulSoup(texto)

## 4. Aplicamos los métodos que ya conocemos: .findAll(), find(), .string
hits = soup.findAll('hit')

output = csv.write(open('BLAST.csv','w'))
output.writerows(['Hit','Evalue'])
for x in hits:
    hsps = x.findAll('hit_hsps')
    for y in hsps:
        print(y.findAll('hsp_num'))
        
    
    
        hit_id = x.find('hit_id').string
        evalue = float(x.find('hsp_evalue').string)
        seq = x.find('hsp_hseq').string
        defi = x.find('hit_def').string
        print(hit_id,defi,evalue,seq)
        output.writerows([hit_id,evalue])
        
