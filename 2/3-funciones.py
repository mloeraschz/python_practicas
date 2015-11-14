#### 2.3 FUNCIONES 
####
#### Más de una vez nos vemos en la ocasión de estar escribiendo
#### una misma línea de código una y otra vez. Crear una función propia
#### nos permite economizar líneas en estas acciones que repetimos.
####
#### Por ejemplo, si debemos obtener promedios constantemente,
#### podemos definir una función para obtenerlos:

def promedio(lista): # La sintaxis indica entre paréntesis el nombre de una
                     # variable local, que será utilizada en la función,
                     # pero no en otras partes del código.
                     
    promedio = sum(lista)/len(lista) # Esta es la fórmula que debemos aplicar.
                                     # Nota cómo utilizamos a la variable local.
                                     
    return promedio                  # Y finalmente, debemos dar return a la
                                     # variable resultado.

#### Vamos a probar a nuestra función

x = [12,32,45,34,62,76,45,34] # Construimos una lista.
p = promedio(x)               # Le aplicamos nuestra función.
print(p)                      # E imprimimos el resultado.


#### Las funciones también pueden operar con variables de cadenas de caracteres.
#### Por ejemplo, una acción que se repite comúnmente es eliminar caracteres
#### indeseados, como dobles espacios, comillas, o hacer transformaciones
#### de minúsculas a mayúsculas.

#### Finalmente, las funciones pueden recibir más de una
#### variable de entrada, las cuales
#### son separadas por comas:

def areaTriangulo(b,h):
    return (b*h/2)

print(areaTriangulo(2,2))


#### Reto1: Define una función que elimine los caracteres: \n \t "
#### y que transforme un texto a mayúsculas.

#### Reto2: Define una función que calcule la desviación estándar de una
#### lista de números. Haz otra función para calcular la mediana.
