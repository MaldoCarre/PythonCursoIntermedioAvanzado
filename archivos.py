#Desarrollar un un script que me liste el contenido de archivos de una carpeta con sus pesos (bytes, kb , mb, etc) y copiar los archivos a otra capeta 
#cambiandole nombre y extensión y el nombre a: <nombre_del_achivo_sin_extension>_ejercicio_python.txt

import os,shutil
def archivos():
    dir = os.getcwd()#obtengo la ubicacion de la carpeta en donde esta mi codigo.
    directorios = os.listdir(dir)# listo todos los arhivos que se encuentran en el
    destino = dir+'/test2' #carpeta de destino
    for i in directorios:
        size = os.path.getsize(dir+'/'+i) # por medio de la lista obtengo los achivos y su peso en bytes.
        print ("archivo: ",i," su peso: ",size,"bytes.")
        if i == 'archivos.py':
            pass
        elif i == 'hola.txt' : #pregunto por el nombre del archivo
            archivo = os.path.join(dir,i) # obtengo el path completo
            shutil.copy(archivo,destino) # indico la carpeta origen (archivo = path completo) y la de destino 
            archivo_destino = os.path.join(destino,i) # me dirijo a la nueva carpeta y al archivo que deseo renombrar
            archivo_renombre = os.path.join(destino,'hola.txt_ejercicio_python.txt') # indico el nuevo nombre
            os.rename(archivo_destino,archivo_renombre) #ejecuto la funcion rename
        elif i == 'chau.py' :
            archivo = os.path.join(dir,i)
            shutil.copy(archivo,destino)
            archivo_destino = os.path.join(destino,i)
            archivo_renombre = os.path.join(destino,'chau.py_ejercicio_python.txt')
            os.rename(archivo_destino,archivo_renombre)
archivos()
