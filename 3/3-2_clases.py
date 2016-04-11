### Clases en Python

### Seguramente te has fijado ya que cuando necesitamos utilizar algunas
### funciones especiales, tenemos que "importar" una biblioteca.
### A lo largo de las sesiones hemos utilizado las bibliotecas "os" y
### "random".

### Estas bibliotecas son compendios que contienen clases
### y funciones que alguien más ya codificó y las puso a disposición
### de la comunidad Python.

### Nosotros también podemos hacer lo mismo con los scripts que usamos
### regularmente. Después de todo: si ya lo codificaste una vez, ¿para qué
### hacerlo otra vez?

### Las clases son estructuras de datos, tal como lo son las listas,
### los diccionarios, las funciones, pero son una estructura de datos especial:
### las clases son la plantilla en la que se crean los objetos.

### Hasta ahora hemos hablado mucho de objetos,¿pero qué son los objetos?
### Simple y llano: son encapsulaciones de variables y funciones.
### Las "clases" son los planos con los que esos objetos son construidos.

### Por ejemplo, supongamos que tenemos un pequeño almacén de
### reactivos químicos en los que tenemos: NaCl, NaOH y Na2SO4.

### Vamos a representar la estructura de nuestro almacén con una clase:

class reactivo(object):
    def __init__(self, formula,MW):
        self.formula = formula
        self.MW = MW

    def compuesto(self):
        print('Este compuesto es: %s' % formula)

    def gramos(self, volumen, molaridad):
        gramos = self.MW * volumen * molaridad
        return gramos

NaCl = reactivo('NaCl',54.44)
print(NaCl.formula)
print(NaCl.MW)
print(NaCl.gramos(1,1))
