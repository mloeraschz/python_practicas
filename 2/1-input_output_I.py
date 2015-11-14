##### 2.1 Input y Output de archivos. Primera parte: INPUT
#####
##### Python puede abrir e interpretar archivos de texto utilizando la función
##### open()
#####
##### archivo = open("dirección del archivo","r")
##### texto = archivo.read()
##### archivo.close()
##### print(texto)
#####
##### Es muy importante escribir el método .close() para que el interpretador
##### cierre el archivo para que el archivo pueda ser usado después
##### sin peligro de borrar nuevos datos y para no saturar a la computadora
##### con archivos abiertos.



archivo = open('BIINEGI_BIINEGI20151108153516.CSV','r', encoding='utf-8')
texto = archivo.read()   #### <---- Fíjate cómo estamos usando el método
                         #### .read() para leer el archivo.
archivo.close()
#print(texto)



archivo = open('BIINEGI_BIINEGI20151108153516.CSV','r', encoding='utf-8')
texto = archivo.readlines()   #### <---- ahora vamos a usar el método
                              #### .readlines() ¿Qué diferencias observas?
                              #### con respecto a .read()
archivo.close()
#print(texto)

#### Si te fijaste bien, el método .read() lee el archivo como una cadena
#### de caracteres.

#### Por otro lado, el método .readline() lee el archivo como una lista,
#### donde cada elemento es una línea del archivo original.

#### RETO!!! Con cada línea del archivo, crea una lista usando el método
#### .split() e imprímela.

#### ¿Lo conseguiste?
#### Si te das cuenta, esto te permite explorar los elementos de cada celda.
#### ¿Qué necesitas para encontrar a algún estado en particular?
#### 1. Hacer accesible las partes relevantes del texto
#### 2. Encontrar la manera de comparar tu variable con las partes relevantes
####    del texto problema.

#### Hasta ahora, ya sabemos cómo hacer el paso 1 (hacer accesible a las partes
#### relevantes del texto). ¿Pero cuál es esa parte relevante?

#### Podriamos utilizar la instancia "in" en un if para encontrarla.

for linea in open('BIINEGI_BIINEGI20151108153516.CSV','r', encoding='utf-8'):
    linea = linea.strip()   #### <---- .strip() remueve los caracteres
                        #### especiales en los flancos.
    
    linea = linea.replace('"','')   #### Aquí eliminamos las comillas
                                    #### que están de más.
    
    if "Nuevo León" in linea: #### <---- aquí usamos la instancia "in" para
                              #### encontrar al estado de Nuevo León.
        print(linea)
    

#### Esta estrategia es útil como exploración primaria, pero ¿cuál de todas
#### las líneas es la que necesitamos? Todavía tenenemos que seguir filtrando
#### los datos.
####

#### Una práctica recomendable es utilizar la instancia "with...as" para
#### asegurar que se manejan todas las excepciones:

####with open('miarchivo.txt','r') as file:
####    do something...

#### Más adelante ahondaremos más en las excepciones.
        
#### Es importante tener en mente que:
####
#### CADA BASE DE DATOS ES DIFERENTE,
#### PERO PODEMOS ENCONTRAR PATRONES
#### Y HACER SCRIPTS PARA EXPLORARLAS.
####
#### Si intentáramos hacer esta misma tarea (extraer la información relevante
#### a algún o algunos estados) con Excel, tomaría algunos
#### clicks hacerlo. Y eso no es difícil si solamente tenemos un archivo para
#### analizar. ¿Pero qué pasaria si tenemos que analizar
#### varias bases de datos? De hecho, tenemos todavía varias bases de datos
#### por analizar.
#### 
#### Para empezar, vamos a explorar nuestras bases de datos y a encontrar
#### patrones que nos sean útiles. A lo largo de esta sesión, aprenderemos
#### cómo aprovechar esos patrones para analizar varios archivos con un
#### solo script.
####
        
