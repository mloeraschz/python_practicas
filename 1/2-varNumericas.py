#####Operaciones con números
#####
##### Las variables también pueden ser numéricas

miNumero = 5 ### este es un entero
otroNumero = 2.5 ### este es un float

##### Para imprimir una variable numérica, es necesario transformarla a string

print(str(miNumero))

##### Las variables numericas pueden usarse en operaciones aritméticas

print(str(miNumero/otroNumero)) ## División usando nombres de variables
print(str(2+3))                 ## Suma
print(str(2-3))                 ## Resta
print(str(2*3))                 ## Multiplicación
print(str(2**3))                ## Potencia
print(str(2/3))                 ## División
print(str(5//2))                ## Floor division
print(str(5%2))                 ## Modulo
print(str(2**0.5))              ## Complemento

##### En Python también existen los operadores de comparación y de equivalencia.
##### Estos operadores devuelven como respuesta: True o False.

print(2>4)                     ## Operador > (mayor que)
print(2<4)                     ## Operador < (menor que)
print(2>=4)                     ## Operador >= (mayor que o igual)
print(2<=2)                     ## Operador <= (menor que o igual)
print(2==4)                     ## Operador == (igual que)
print(2!=4)                     ## Operador != (diferente que)

##### Otros operadores muy útiles son los operadores de asignación
##### Estos operadores economizan la transformación del valor de una variable.

##### Supongamos que tenemos una variable inicial "miNumero".

miNumero = 5

##### Ahora necesitamos multiplicarla por 2. Podríamos entonces escribir
##### miNumero = miNumero * 2
##### Pero recordemos que en Python, entre más simple, mejor.
##### Así que existe la posibilidad de hacer esa misma operación asi:

miNumero *= 2                     ## Multiplicando por 2
print(miNumero)

miNumero += 10                    ## Sumando 10
print(miNumero)

miNumero /= 2                     ## Dividiendo entre 2
print(miNumero)

miNumero -= 5                     ## Restando 5
print(miNumero)

##### RETO!!!! Imprime el promedio de los siguientes números: 10,15,20









