##### MANEJO DE ERRORES COMUNES
#####
##### Algunas veces cuando corremos un bucle for, existe en un punto en el que
##### se genera un error y el loop se detiene por completo.
##### Por ejemplo, cuando se hace mención a un elemento que no existe en una
##### lista, el script se detiene y lanza un IndexError o ValueError
##### ¿Pero qué podemos hacer para que el script siga corriendo y no deje
##### la tarea incompleta?
#####
##### La solución: declarar y marcar una excepción para los tipos de error que
##### esperamos que sucedan.
#####
##### Por ejemplo, intenta corriendo el siguiente script.
##### ¿Qué es lo que aparece? 

lista = [1,2,3,4,5,"a",7,8,9,10]
for elemento in lista:
    resultado = elemento + 2
    print(str(resultado))

##### Ahora intenta con el siguiente script. ¿Qué es lo que observas que
##### es diferente?

lista = [1,2,3,4,5,"a",7,8,9,10]
for elemento in lista:
    try:
        resultado = elemento + 2
        print(str(resultado))
    except TypeError as detail:
        print('Something went wrong: %s\n' % elemento, detail)


##### Acabamos en de observar el efecto de la declaración "try"..."except",
##### y de paso también la de la declaración "as" y "%s".

##### Actividad: escribe las excepciones adecuada para que el siguiente loop
##### funcione hasta el último elemento de la lista "numeros".

numeros = [0,1,2,3,4,5,6,x,8,9,"y",11]
for numero in numeros:
    print(1 + (1/numero))

#### Ya habíamos visto cómo funcionan los enunciados "with...as..."
#### Estas instancias nos permiten sortear los errores que emergen luego de
#### abrir un archivo. La sintaxis es la siguiente:

with open('miArchivo.txt','r') as file:
    texto = file.read()
    print(texto)

#### Y listo. Sin necesidad de escribir try... except si ocurre algún Error.
#### Al final del script, cualquier error que ocurrió dentro del enunciado
#### "with...as" es reportado en la shell. Y además, ¡no es necesario
#### escribir .close()! El enunciado "with...as" lo hace por si mismo.
