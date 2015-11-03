#!/usr/bin/python
##### LIST COMPREHENSION
#####
#####
##### En Python pueden generarse listas automáticamente utilizando
##### "List comprehension" (comprensión de listas)
##### 
import math

aa = [x for x in range(0,100)]
ab = [x**2 + 2*x + 2 for x in range(0,100)]


###with open('try.csv','wt') as csvfile:
###    csvFile = csv.writer(csvfile)
###    for x,y in zip(aa,ab):
###        row = str(x),str(y)
###        csvFile.writerow((str(x),str(y)))


### Si te diste cuenta, también hicimos una función para escribir un archivo
### de texto con el resultado de las dos listas.


