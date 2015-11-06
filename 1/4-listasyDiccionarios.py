##### LISTAS Y DICCIONARIOS

#####
#####
#####
##### En Python pueden crearse listas de elementos como
##### variables, strings, números, entre otros.
##### La manera de escribir, o sintaxis, de una lista es la siguiente:

miLista = ["Elemento1","Elemento2","Elemento3","Elemento4","Elemento5"]

print(miLista)

##### Si queremos agregar un elemento a una lista, se debe hacer lo siguiente.

nuevoElemento = "Hola"              #Primero instanciamos el nuevo elemento.

miLista.append(nuevoElemento)       #Nuestra lista ya está instanciada, así
print(miLista)                      #que solamente tenemos que agregar el
                                    #nuevo elemento con el método ".append"



##### Si queremos remover elementos, podemos aplicar los siguientes métodos:

miLista.remove("Elemento4")         #El metodo ".remove" quita el elemento
print(miLista)                      #especificado entre los paréntesis.

miLista.pop(2)                      #El metodo ".pop" quita el elemento
print(miLista)                      #ubicado en la posición especificada
                                    #entre los paréntesis. Recuerda que
                                    #la numeración inicia desde el 0!

##### Algunos métodos para re-organizar las listas, son:


miLista.sort()                      #El metodo ".sort" ordena a los elementos
print(miLista)                      #por orden alfabético.

miLista.reverse()                    #El metodo ".reverse" ordena a la lista
print(miLista)                      #de fin a inicio
                                    

##### Las listas es un tipo de estructuras de datos que Python soporta.
##### Otros tipos de estructuras de datos muy útiles son los diccionarios.
##### Los diccionarios contienen información relacional, es decir,
##### cada elemento tiene asignados "keys" o "llaves" que llevan a
##### a la información.

##### Por ejemplo, supongamos que tenemos una pequeña base de datos con
##### informacion sobre tres personas: edad, país y teléfono.
##### Esto lo podemos poner en tres diccionarios de la siguiente manera:

Ana = {'edad':20,'pais':'Perú','telefono':'12345'}

#####  Ahora hagamos lo mismo con dos personas más:

Jose = {'edad':26,'pais':'Venezuela','telefono':'34567'}
Francisco = {'edad':22,'pais':'México','telefono':'45678'}

##### Si queremos imprimir la edad de José, haríamos lo siguiente:
print(Jose['edad'])

##### RETO!!!! Imprime el país de cada uno de los diccionarios.

##### Ahora nos gustaría agregar la ciudad de procedencia de cada persona.
##### Para agregar más información a un diccionario, puedes hacer lo siguiente.

Ana['ciudad'] = 'Lima'


##### RETO!!!! Agrégales una ciudad a José y Francisco e imprime los nuevos
##### diccionarios.


##### Otra manera de crear diccionarios es usando el metodo ".fromkeys".
##### Primero debemos crear una lista con el nombre de nuestras keys.
##### Esta vez lo haremos para especificar la base y altura de un triángulo.

triKeys = ['base','altura']

##### Ahora usamos el metodo ".fromkeys" para crear un diccionario vacío.

triangulo = dict.fromkeys(triKeys, [10,50])
print(triangulo)

##### RETO!!!! Asígnales los siguientes valores a las keys del triángulo:
##### base = 20 y altura = 50. Luego encuentra el área del triángulo
##### e imprímela.

##### DE STRING A LISTA Y VICEVERSA
##### 
##### La función "list" y el método ".join" permiten transformar variables de 
##### cadenas de caracteres en listas, y viceversa, respecetivamente.
##### 
##### Por ejemplo, supongamos que se tiene la siguiente variable de cadena de
##### caracteres:

pal = 'palabra'

##### Para transformarla a una lista cuyos elementos sean cada letra, basta con utilizar
##### la función "list":

pal = list(pal)
print(pal)

##### Y al contrario, para transformar una lista de vuelta a string, se puede utilizar
##### el método ".join".

pal = ''.join(pal)
print(pal)

##### Si te fijas, antes del método ".join" se escribieron dos comillas '' 
##### Esto es porque dentro de estas comillas se especifica el caracter que
##### habrá de unir a la lista. En nuestro caso, ningún caracter fue especificado,
##### por lo que el método ".join" unió a los elementos de la lista sin ningún
##### caracter entre ellos.


##### TUPLES
##### 
##### Otra estructura de datos que soporta Python, son los tuples. Estas estructuras son
##### similares a las listas, con la diferencia de que no se pueden cambiar una vez
##### instanciados. Es decir, el método ".replace" no funciona con las tuples.
##### También, la sintaxis es diferente:

miTuple = ('elemento1','elemento2','elemento3')

##### Los tuples son útiles cuando se necesita especificar un vector de datos
##### constante.
