#Realizar una funci´on que retorne la suma de todos los m´ultiples de 3 y 5, en el rango de 0 a X.

def suma():
    suma = 0
    for i in range(0,int(input("intrduzca valor: "))):
        if (i % 3 == 0) and (i % 5 == 0):
            suma += i
    return print ("El valor de la suma de numeros de 0 a X es:",suma)
suma()