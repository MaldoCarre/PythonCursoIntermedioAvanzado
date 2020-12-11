# Escribir una función que ordene una lista de tuplas por el segundo elemento de la tupla.
# Por ejemplo:
# Entrada : [(2, 8), (1, 2), (4, 4), (2, 3), (2, 1)]Salida : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 8)]

def menorMayor ():
    entry = [(2, 8), (1, 2), (4, 4), (2, 3), (2, 1)] #recibo mi entrada. 
    print("Entrada: ",entry)
    base = [i[1] for i in entry] # guardo el segundo valor da cada tupla en una lista nueva.
    base.sort() # Ordeno de menor a mayor los valors de esta nueva lista.
    salida =[j for i in base for j in entry  if i == j[1]] # recorro los valores ordenado , comparo con entrada y ordeno salida.
    return print("Salida: ",salida)
menorMayor()


