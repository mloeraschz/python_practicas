## 3.3 Navegación web - Primera Parte
##
## Existen bibliotecas de Python que permiten explorar el Internet a través
## de scripts. Sin embargo, el tipo de biblioteca a emplear y los métodos
## para acceder y utilizar las páginas web, depende de la página que
## visitemos. No todas las páginas permiten acceso directo a todos los
## componentes. Otras, necesitan input de JavaScript para ser operadas.
## En esta sesión aprenderemos los métodos básicos de la biblioteca "urllib",
## la cual nos permite explorar páginas web que no requieren de JavaScript
## y que no tienen restricciones de acceso.
import re
import urllib
import urllib.request # Primero, debemos importar la librería urllib y
                    # específicamente, el método ".request", el cual nos
                    # permitirá acceder a la página.



url = 'http://www.fcb.uanl.mx/nw/es/acerca-de-la-fcb/profesores'
# Está es la página web que queremos visitar.

with urllib.request.urlopen(url) as response: # ¿Recuerdas la expresión
                                                  # "with...as"? Aquí
                                                  # la utilizamos para utilizar
                                                  # el método urllib.request.urlopen()

   pagina = response.read()                       # El método .read() permite
                                                  # interpretar le objeto creado
                                                  # con el nombre "response".
                                                  
   pagina = pagina.decode('utf-8')                # Finalmente, la página
                                                  # es decodificada como
                                                  # un texto utf-8 que contiene
                                                  # el código html de la web.
 
#print(pagina)

## Otro método de la biblioteca urllib, es .request.urlretrieve
## que permite almacenar una copia del contenido de una url
## en un archivo local. En pocas palabras: permite bajar archivos.
## Intenta correr el siguiente script.

#urllib.request.urlretrieve('http://www.fcb.uanl.mx/esp/imagenes/vscacomixtlesin2.gif','imagen.gif')

## Como te puedes dar cuenta, la exploración de páginas web involucra
## operaciones con cadenas de caracteres y escribir código adecuado a cada caso,
## dependiendo de nuestro propósito al explorar la web.
## Los archivos html pueden ser interpretados utilizando expresiones
## regulares para cada tipo de tags. Esto permite automatizar la extracción
## de datos de más de una página dentro de un servidor. Pero esto se vuelve
## complicado muy pronto. 
                                                  
## En las siguientes sesiones seguiremos trabajando con operaciones en la web.
## y cómo hacer más sencilla la interpretación (parsing) de html.                                                
## Por lo pronto, vamos a concluir esta introducción con un par de ejercicios:

## 1. Imprime todos los links contenidos en la página web http://www.fcb.uanl.mx/nw/es/
##    Recuerda que el tag <a href=''> indica la presencia de un link.
## 2. Guarda todas las imágenes que encuentres en esa misma página
##    Recuerda que el tag <img src=''> indica la presencia de una imagen.
