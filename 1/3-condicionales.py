##### CONDICIONALES
#####
#####
#####


##### Una de las operaciones más frecuentes en los scripts de Python
##### es el uso de condicionales para controlar el flujo de scripts.
##### Estas operaciones condicionales pueden traducirse al lenguaje
##### cotidiano como "si X cumple con Y entonces haz Z"

##### Por ejemplo, iniciemos con una variable numérica que el usuario debe
##### escribir:

#miVariable = input("Escribe un número entero: ")
#miVariable = int(miVariable)        ##### Esta línea de codigo transforma
                                    ##### una variable string a número.
                                    ##### La función input siempre produce
                                    ##### una variable string.
                                    ##### De otra manera, obtendríamos
                                    ##### un TypeError.


    

##### Ahora, supongamos que el usuario escribio un número y
##### queremos decirle al usuario que su número es un par. ¿Cómo podemos
##### hacerlo? Pues simple: si dividimos un número entre 2 y no hay residuo.
##### Para esto usamos la función módulo y una operación condicional.
##### En lenguaje cotidiano, queremos decirle a la computadora lo siguiente:
##### "si miVariable cumple con miVariable%2==0 entonces
#####  imprime que el número es un par".

##### En lenguaje Python, eso se traduce a:
#if miVariable % 2 == 0:
#    print("El número es un par")

##### ¿Cómo podriamos informarle al usuario que el número es impar?
##### La solución es usando la siguiente expresión. (Borra los hashtags
##### cuando se te indique).
#####else:
#####    print("El número es un impar")

##### Si quisiéramos agregar una condición alternativa, podemos utilizar
##### la instancia "elif".
##### Por ejemplo, tomemos esta lista de números:

#miLista = [1,2,3,4,5,6,11,22,33,44,55,66]

#for x in miLista:
#    if x % 3 == 0 and x % 2 == 0:
#        print("%s es divisible entre 2 y 3" % x)
    
#    elif x % 2 == 0:
#        print("%s es divisible entre 2" % x)
#        
#    elif x % 3 == 0:
#        print("%s es divisible entre 2" % x)
#    else:
#        print("%s no es divisible entre 2 o 3" % x)



