### 3.1 Expresiones regulares

### El análisis de textos requiere de funciones especializadas en
### reconocer patrones. Estas funciones de reconocimento de patrones
### están reunidas en la biblioteca "re", o "regular expressions".

### Los métodos básicos de la biblioteca "re" son "re.match()", 
### "re.search()" y "re.findall()".

### El método "re.match()" ayuda a encontrar patrones al inicio de una cadena
### de caracteres.

import re
texto = '''Nuevo León, Tamaulipas, Oaxaca'''
patron = re.match(r'nuevo le[óo]n',texto,flags=re.IGNORECASE)
                        ### ¿Observas cómo usamos re.IGNORECASE para hacer
                        ### la búsqueda insensible mayúsculas y minúsculas?
                        ### También observa cómo creamos un grupo [óo] para
                        ### que la expresión regular busque tanto una "ó" como
                        ### una "o" en una determinada posición.
print(patron)  ### Crea un objeto donde se contiene la cadena de caracteres
               ### que coincide con el patrón. 
#print(patron.group(0)) ### El objeto contiene "grupos", y el grupo 0 es el que
                       ### contiene la cadena que coincide con nuestro patrón.
                       ### Como estamos utilizando el método re.match(), siempre
                       ### se analizará solamente el inicio de la cadena
                       ### original. Intenta usar re.match() para buscar
                       ### "Tamaulipas" con el mismo código. ¿Qué sucede?
        
        
### Ahora probemos qué hace el método re.search(). Para eso, vamos a abrir
### un archivo.

with open('BIINEGI_BIINEGI20151108153516.CSV','r',encoding='utf-8') as file:
    lineas = file.read()
    
    patron = re.search(r'nuevo le[óo]n',lineas,flags=re.IGNORECASE)
    print(patron)
    print(patron.group(0))

### El método re.search() permite buscar más allá del inicio de la cadena de
### caracteres, pero se detiene cuando encuentra un match.

### Si queremos encontrar todas las veces que una expresión regular aparece
### en un texto, debemos usar el método re.findall()
        
with open('BIINEGI_BIINEGI20151108153516.CSV','r',encoding='utf-8') as file:
    lineas = file.read()
    
    patron = re.findall(r'nuevo le[óo]n',lineas,flags=re.IGNORECASE)
    print(patron)

### El método re.finditer produce un objeto iterable.
### Observa cómo usamos el método .span() para obtener la ubicación de la
### expresión regular.

with open('BIINEGI_BIINEGI20151108153516.CSV','r',encoding='utf-8') as file:
    lineas = file.read()
    it = re.finditer(r'nuevo le[óo]n',lineas,flags=re.IGNORECASE)
    for match in it:
        print("'{g}' was found between the indices {s}".format(g=match.group(), s=match.span()))
        
### Finalmente, un método para sustituir cada elemento que coincide con la
### expresión regular, es el método "re.sub()". Aquí lo observamos en acción:

texto = '''Nuevo León, Tamaulipas, Oaxaca'''
texto = re.sub(r'nuevo le[óo]n', 'NL',texto,flags=re.IGNORECASE)
print(texto)

### Las expresiones regulares son una herramienta versátil que puede
### extenderse a aplicaciones mucho más complicadas que las que vimos.
### A lo largo del curso, abordaremos algunas de esas aplicaciones
### durante las sesiones de parsing de xml y html.

### A continuación, un ejemplo de esas aplicaciones avanzadas. Este es un
### ejemplo de la aplicación de expresiones regulares para encontrar las
### cadenas de caracteres de un texto que coinciden con la estructura
### de un correo electrónico.

texto = '''Mi correo electrónico es x@ejemplo.com y mi otra dirección es y@bambi.edu.mx Mi tel. es 111-111-1111'''
regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
patron = re.findall(regex,texto)
print(patron)


