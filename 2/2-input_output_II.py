#### INPUT Y OUTPUT
#### SEGUNDA PARTE: OUTPUT
####
#### Anteriormente aprendimos cómo abrir y leer un archivo de texto usando
#### Python. Esto es útil cuando necesitamos acceder a bases de datos o
#### cualquier archivo donde haya información que necesitamos.
####
#### Pero nuestros scripts también generan información importante para nosotros
#### y también existen maneras para escribir nuestros propios documentos
#### con scripts de Python.
####
#### La manera para hacerlo es similar a la del input de archivos:
#### debemos abrir un documento utilizando la función "open()", pero esta vez
#### en lugar de instanciar el modo "r", instanciaremos el modo "w" o "a".
####
#### Supongamos que tenemos una variable de texto que queremos guardar en un
#### archivo aparte.

texto = 'áéíóúäöü'

#### Ahora debemos únicamente abrir una ubicación para nuestro archivo output.
#### No importa que no exista el archivo todavía: la función "open()" funciona
#### como si se abriera un archivo en blanco.

output = open('miOutput.txt','w') # Nota cómo escribimos la extensión.
                                  # La dirección del archivo también puede
                                  # ser especificada si no queremos grabarla
                                  # en el mismo folder que nuestro script:
                                  # C:\\Direccion...

output.write(texto)               # El metodo ".write()" nos permite escribir
                                  # la variable de texto en el archivo que
                                  # hemos abierto.

output.close()                    # IMPORTANTE! No olvides cerrar tu archivo.

#### Comprueba que tengas un archivo de nombre 'miOutput.txt' en tu
#### folder.

#### Cambia el valor de la variable "texto" por cualquier otro string.
#### Corre el script y observa el resultado. ¿Qué sucedió?

#### Ahora intenta hacer lo mismo utilizando el modo "a", en lugar de
#### el modo "w", ¿qué diferencia observas en el resultado?

#### Anteriormente vimos cómo crear una función. Cuando tenemos que estar
#### grabando constantemente los resultados de nuestro script, es útil tener
#### una función que lo haga.

def escribir(texto,nombreArchivo, extension,modo):
    output = open(nombreArchivo + '.'+ extension,modo)
    output.write(texto)
    output.close()
    
#### Intenta escribir un archivo usando nuestra función escribir()

escribir('bambi','bambi','txt','w')
