## 4-3 Tkinter
##
## Hasta ahora hemos trabajado código directamente en el editor. Esto puede ser
## sencillo para quienes ya conocen de programación, pero existen usuarios
## que no tendrán idea de cómo utilizar nuestros scripts.

## Para permitir que más personas puedan usar un programa, se necesitan
## interfaces gráficas para usuarios o GUI, como ventanas, botones,
## campos de texto, etc.

## Tkinter es una biblioteca de Python que permite crear GUIs de manera 
## intuitiva.
##

import Tkinter      # Aquí importamos la biblioteca.
from Tkinter import *
top = Tk()  # Ahora creamos una ventana
top.wm_title('Mi GUI') # Le ponemos un título
top.geometry('{}x{}'.format(300, 500)) # Le especificamos el tamaño
#top.mainloop()      # Y lo accionamos.


## BOTONES
## Para crear un botón en tkinter, basta con usar la función Button:
## boton = Tkinter.Button(master, text, command...)


def funcion():
    print('Hola!')

boton = Button(top,text='Para muestra un botón', command=funcion)
boton.pack() # No olvidemos incluir al botón en "top" con el método .pack()

#top.mainloop()

## SELECCIONAR ARCHIVOS

## Cuando necesitamos abrir un archivo, debemos escribir la dirección entera
## en nuestro código. ¿Podríamos hacerlo de una manera más sencilla?
## Vamos a usar la clase tkFileDialog

import tkFileDialog

def leerArchivo():
    texto = tkFileDialog.askopenfile(mode='r') # con este comando, abrimos el archivo
                                               # y lo asignamos a la variable 'texto'
    print(texto)
    
boton = Button(top,text='Leer archivo', command=leerArchivo)
boton.pack()
#top.mainloop()




## ROTULACIONES
##
## Para darle instrucciones al usuario e identificar cada parte de la GUI
## podemos utilizar rotulaciones o "labels".

texto = StringVar()
label = Label(top,textvariable=texto,relief=FLAT)
texto.set('Estás utilizando mi GUI')
label.pack()
#top.mainloop()


## LISTAS
##
## Las listas permiten dar opciones al usuario para elegir. Esto es útil cuando
## se tiene un conjunto de opciones predefinidas y que no aceptan
## elementos diferentes.

lista = Listbox(top, selectmode=SINGLE)
lista.insert(1,'Primer elemento')
lista.insert(2,'Segundo elemento')
lista.insert(3,'Tercer elemento')
lista.insert(4,'Cuarto elemento')
lista.pack()
#top.mainloop()

## TEXTO
##
## Si quieres que tu GUI acepte texto de tu usuario, puedes utilizar la función
## Entry():

lb = Label(top,text='Escribe algo: ',relief=FLAT)
lb.pack()
texto = Entry(top,bd=5)
texto.pack()
def txt():
    print(texto.get())
bt = Button(top,text='Imprimir',command=txt)
bt.pack()

#top.mainloop()

## CALLBACKS
##
## Muy bien. Creamos una lista. Ahora hay que hacerla funcionar: debemos asignarle
## una acción, o callback. Para eso utilizamos el método .bind()

def seleccion(evento): # Primero definimos la acción que queremos que suceda:
                       # a manera de ejemplo, vamos a imprimir lo que el usuario
                       # seleccionó                    
    
    handler = evento.widget # el método .widget crea nuestro evento
    index = int(handler.curselection()[0]) # obtenemos el índice de la selección
    value = handler.get(index) # Y finalmente, obtenemos el valor de la selección
    print('Seleccionaste el elemento %d: "%s"' % (index, value))


#lista.bind('<<ListboxSelect>>', seleccion)
#top.mainloop()

## ACTIVAR/DESACTIVAR BOTONES

## Algunos botones deben permanecer inactivos hasta que una acción se haya completado.

## Primero, vamos a crear un botón inactivo:
def hola():
    print('Haz activado el botón!')

b = Button(top,text='Boton activable',state=DISABLED,command=hola)
b.pack()
#top.mainloop()

# Ahora vamos a hacer que se active cuando se seleccione algo de la listbox.

def selLista(evento):
        
    handler = evento.widget # nuevamente creamos un evento
    b.config(state='normal') # Y este es el cambio que observaremos en nuestro
                             # botón cuando suceda el evento.
      

#lista.bind('<<ListboxSelect>>', selLista) # Conectamos nuestra función
                                          # con la listbox y damos .mainloop()
#top.mainloop()

                                          

