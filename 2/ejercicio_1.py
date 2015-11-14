with open('codones.txt','r') as archivo:  ## Abre el archivo de la tabla de codones
    texto = archivo.readlines()
    
codones = {}   ### Diccionario de codones
for i in texto:
    i = i.strip() ### Remueve saltos de linea y otros caracteres especiales
    linea = i.split('\t') ### Transforma cada linea en una lista, dividiendo en cada tab
    trip = linea[1].replace(' ','') # Remueve los especios en blanco del segundo elemento de la lista
    trip = trip.split(',') # Divide el segundo elemento en otra lista, dividiendo en cada coma
    for j in trip:
        codones[j] = linea[0] # Asigna cada codon de la lista trip al aminoacido (primer elemento
                              # de la lista 'linea'

print(codones)

secuencia = '''ATGACAAAGTATGCATTAGTCGGTGATGTGGGCGGCACCAACGCACGTCTTGCTCTGTGTGATATTGCCA
GTGGTGAAATCTCGCAGGCTAAGACCTATTCAGGGCTTGATTACCCCAGCCTCGAAGCGGTCATTCGCGT
TTATCTTGAAGAACATAAGGTCGAGGTGAAAGACGGCTGTATTGCCATCGCTTGCCCAATTACCGGTGAC
TGGGTGGCGATGACCAACCATACCTGGGCGTTCTCAATTGCCGAAATGAAAAAGAATCTCGGTTTTAGCC
ATCTGGAAATTATTAACGATTTTACCGCTGTATCGATGGCGATCCCGATGCTGAAAAAAGAGCATCTGAT
TCAGTTTGGTGGCGCAGAACCGGTCGAAGGTAAGCCTATTGCGGTTTACGGTGCCGGAACGGGGCTTGGG
GTTGCGCATCTGGTCCATGTCGATAAGCGTTGGGTAAGCTTGCCAGGCGAAGGCGGTCACGTTGATTTTG
CGCCGAATAGTGAAGAAGAGGCCATTATCCTCGAAATATTGCGTGCGGAAATTGGTCATGTTTCGGCGGA
GCGCGTGCTTTCTGGCCCTGGGCTGGTGAATTTGTATCGCGCAATTGTGAAAGCTGACAACCGCCTGCCA
GAAAATCTCAAGCCAAAAGATATTACCGAACGCGCGCTGGCTGACAGCTGCACCGATTGCCGCCGCGCAT
TGTCGCTGTTTTGCGTCATTATGGGCCGTTTTGGCGGCAATCTGGCGCTCAATCTCGGGACATTTGGCGG
CGTGTTTATTGCGGGCGGTATCGTGCCGCGCTTCCTTGAGTTCTTCAAAGCCTCCGGTTTCCGTGCCGCA
TTTGAAGATAAAGGGCGCTTTAAAGAATATGTCCATGATATTCCGGTGTATCTCATCGTCCATGACAATC
CGGGCCTTCTCGGTTCCGGTGCACATTTACGCCAGACCTTAGGTCACATTCTGTAA'''

secuencia = secuencia.replace('\n','')  # Remueve espacios en blanco
inicio = 0 # Inicio de codon (recuerda que la posicion inicia siempre en 0)
fin = 2 # Final de codon

longitud = len(secuencia)/3 # Numero de codones presente en la secuencia

proteina = '' # A esta proteina se le van a ir agregando los aminoacidos que se traducen del
              # loop for que sigue.

for i in range(0,int(longitud)): # Loop para el total de codones en la secuencia
    codon = secuencia[inicio:fin+1:] # Esta es una variable pivote para cada codon
    proteina += codones[codon] # A la variable proteina se le agrega el valor de cada
                               # codon en el diccionario 'codones'
    
    inicio += 3 # Aumenta el valor para pasar al siguiente codon
    fin += 3

with open('proteina.fasta','w') as file:
    file.write('>Proteina\n')
    file.write(proteina)
          
