####### FOR AND WHILE LOOPS
#######
#######
####### Muchas tareas en programación son repetitivas. Es decir,
####### consisten en la aplicación de una misma actividad para múltiples datos.
####### Para poder automatizar estas actividades, se utilizan los bucles
####### de iteración, o loops.
#######
####### Los dos tipos básicos de loops en Python son: for y while.
#######
####### Empecemos por el while loop.
####### Este bucle consiste en repetir una actividad dependiendo
####### de una condición. En lenguaje cotidiano, el while loop hace lo sig.:
####### "Realiza X acción mientras se cumpla (o no) la condición Y".
#######
####### Por ejemplo, supongamos que queremos en un formulario solamente
####### podemos elegir una de tres opciones A,B o C.

####### EJEMPLO: FORMULARIO PARA NÚMERO DE PÉTALOS
ej = '''
import time
petalos = ''

while petalos != "A" and petalos != "B" and petalos != "C":
    petalos = input("¿Cuál es el divisor mínimo del número de pétalos de la flor? \nA) 4\nB) 5\nC) 3\n")
    petalos = petalos.upper()
    if petalos != "A" and petalos != "B" and petalos != "C":
        print("Por favor, escribe A, B o C")
        time.sleep(1)
    else:
        time.sleep(1)
        
if petalos == "A":
    print("Tu flor es una dicotiledónea")

elif petalos == "B":
    print("Tu flor es una dicotiledónea")

elif petalos == "C":
    print("Tu flor es una monocotiledónea")
'''

####### Los loop for son utilizados para iterar una acción en una lista
####### o diccionario.

####### EJEMPLO: LISTA DE BACTERIAS

bacterias = ['Escherichia coli', 'Bacillus subtilis', 'Bacillus cereus','Clostridium difficile','Streptococcus pneumoniae','Staphylococcus aureus']

for bacteria in bacterias:
    print(bacteria)

####### RETO!!! Imprime solamente los nombres de las bacterias del
####### género Bacillus. Luego, imprime los nombres de las bacterias
####### que no son del género Bacillus.

####### Las listas también pueden ser de números.

calif = [22,25,62,36,86,55,10,61,71,74,58,0,61,79,93,11,96,97,17,67,88,69,0,79,57,19,46,27,30,50,12,55,51,30,20,83,59,64,7,95,49,95,88,81,59,78,4,14,34,55]

####### RETO!!! Obtén el promedio de las calificaciones de la lista "calif",
####### utilizando lo que conoces acerca de los loops for.

suma = 0
N = len(calif)
for x in calif:
    suma += x
promedio = suma/N
print(str(promedio))


####### Una función útil es la función zip()
####### Esta función sirve para iterar a través de dos listas al mismo tiempo.

campos = ['nombre','carrera','semestre']
alumno1 = ['Miguel','LBG','10+6']

alumDict = {}
for x,y in zip(campos, alumno1):
    alumDict[x] = y
print(alumDict)


####### ACTIVIDAD 1:
####### 1) CREA UNA LISTA QUE CONTENGA UN DICCIONARIO POR CADA ALUMNO
#######    DE ESTE CURSO. LAS KEYS SERÁN: 'nombre', 'carrera','semestre'
#######    PISTA: UTILIZA UN FOR LOOP ADENTRO DE OTRO FOR LOOP (LOOP ANIDADO)
#######    Y RECUERDA QUE LA FUNCIÓN zip() PERMITE ITERAR A TRAVÉS DE DOS LISTAS.
####### 2) CREA SUB-LISTAS CON LOS NOMBRES DE LOS ALUMNO QUE PERTENECEN
#######    A UNA CARRERA.
####### 3) IMPRIME CADA SUB-LISTA.

alumnos = [['bambi','LBG','3'],['bambi2','LCA','4'],['bambi3','BIO','5'],['bambi4','QBP','7']]
alumDictList = []
for x in alumnos:
    alumDict = {}
    for y,z in zip(x,campos):
        alumDict[z] = y
    alumDictList.append(alumDict)

for alum in alumDictList:
    if alum['carrera'] == 'LBG':
        print(alum['nombre'])     
