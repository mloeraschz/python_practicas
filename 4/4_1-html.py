## Tema 4-1: Parsing de html con BeautifulSoup
##
## Para extraer la información de un documento html, necesitamos interpretarlo
## o "parsearlo". Podríamos construir nuestro propio interpretador, utilizando
## las herramientas que ya conocemos, pero elaborarlas requiere de atención
## a sinnúmero de detalles y, en consecuencia, tiempo. Afortunadamente,
## existe una biblioteca que permite parsear html y también xml: BeatifulSoup.
##
## Vamos a importarla:

import urllib2
from bs4 import BeautifulSoup

## Ahora, vamos a abrir una url. Puede ser cualquier url que pueda ser explorada
## por urllib2 (recuerda las limitaciones que hablamos en la sesión anterior).
## Bs4 funciona en Python 2.7, por lo que la biblioteca urllib2 también
## funciona de manera diferente.

## urllib2 en Python 2.7  necesita del método ".urlopen()"
## para acceder a una url.

url = 'https://en.wikipedia.org/wiki/Monterrey'
html = urllib2.urlopen(url)
html = html.read()

## La variable html contiene el código de la url que abrimos. Ahora, a este
## html lo vamos a introducir dentro de la función BeautifulSoup. Esta función
## creará un objeto que contiene la interpretación del código html.

soup = BeautifulSoup(html) ## Aquí estamos creando el objeto con el html
                            ## parseado.

## El objeto ahora puede ser utilizado para ser explorado y extraerle
## información utilizando diferentes métodos. En esta sesión
## vamos a practicar con algunos de ellos.

#####################
#####################


## MÉTODOS  PARA INTERPRETACIÓN DE HTML

## Bs4 ya tiene algunos métodos que permiten interpretar el código html y acceder
## a la información en cada tag. Por ejemplo, si queremos acceder al primer
## tag <title> podemos simplemente escribir .title luego de nuestro objeto.

print(soup.title)

## ¿Pero no cómo extraer el texto dentro de ese tag? Hay que agregar el método
## .string

print(soup.title.string)

## Para acceder a otras partes del html, podemos hacer lo mismo:
print(soup.h2) ## Accede a todos los h2
print(soup.h2.parent) ## El método .parent nos permite acceder al tag
                      ## que contiene al h2, es decir, su "parent".

print(soup.p) ## Accedemos a el primer tag p

#####################
#####################


## MÉTODOS FIND / GET:

## Existen dos métodos para encontrar tags y atributos específicos:
## el método .find() y el método .findAll()

## El método .find() permite encontrar a la primera mención del tag
## que coincida con nuestras especificaciones


print(soup.find('span',attrs={'class':'flagicon'})) ## Como te puedes dar
                                        ## cuenta, con .find() podemos especi-
                                        ## ficar incluso los atributos del tag.


## A diferencia del método .find(), el método .findAll devuelve un objeto
## iterable y no una variable de texto:

#parrafos = soup.findAll('p')
#for x in parrafos:              ## Un objeto iterable es exlorable con un loop
#    print(x.get_text())         ## Finalmente, el método .get_text()
                                ## nos permite acceder al texto dentro de
                                ## tags.

## También podemos encontrar textos especificando la búsqueda:
## vamos a imprimir solamente los párrafos que mencionen a Tigres o Rayados
## en la wiki de la ciudad de Monterrey.

import re

parrafos = soup.findAll(text=re.compile(r'(rayados)|(tigres)',re.IGNORECASE))

## ¿Notas cómo usamos una expresión regular en lugar de un texto preciso?
## Podríamos también haber escrito:
## parrafos = soup.find_all(text='tigres')
## pero esto no nos habría permitido ignorar mayúsculas y minúsculas, ni tam-
## poco incluir a los rayados en la búsqueda.

print(parrafos)

## Esto funciona, pero solamente accedemos a las frases donde aparece
## nuestro texto de interés: no tenemos acceso al párrafo entero. Esto lo
## podemos corregir de la siguiente manera:

for x in soup('p'): ## Esto es equivalente a escribir soup.findAll("p")
    if re.search(r'(rayados)|(tigres)',x.get_text(),re.IGNORECASE):
        print(x.get_text()+ '\n\n')

#####################
#####################

## EXPLORANDO TAGS

## Cuando creamos un objeto con .findAll, creamos una estructura similar
## a la inicial (soup). Por lo tanto, podemos explorarla utilizando
## métodos similares.

## Por ejemplo,

tables = soup.findAll('table') ## Encontramos todos las tablas
for table in tables[:2]:           ## Iteramos a través de todas las tablas
    tds = table.findAll('td')  ## Encontramos todos los td (celdas)
    for td in tds:
        print(td.text)        ## td.text es similar a td.get_text()
    


## O si queremos encontrar un tag en específico dentro de la jerarquía,
## podemos usar .findNext(tag)
        
tables = soup.findAll('table') 
for table in tables[:2]:        
    Nth = table.findNext('th') 
    print(Nth.text)
    
        

    

## Retos:
##
## 1. Encuentra todos los urls de las imágenes de la página
## 'https://en.wikipedia.org/wiki/Monterrey'
##
## 2. Encuentra la tabla que tiene este atributo: class="infobox geography vcard"
##
## 3. En la página https://es.wikipedia.org/wiki/Municipios_de_México
## está un listado de los estados, que a su vez, redirigen a una página
## donde está una lista de todos los municipios de cada estado.
## ¿Puedes scrapear el nombre de los presidentes municipales de todos
## los municipios de todos los estados?
