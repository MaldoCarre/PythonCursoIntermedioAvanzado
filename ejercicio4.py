#  La secuencia de fibonacci tiene la siguiente forma: F1 = 1F2 = 1F3 = 2F4 = 3F5 =
# 5F6 = 8F7 = 13F8 = 21F9 = 34F10 = 55F11 = 89F12 = 144 Observamos que en la
# posici´on 12 (11 si comenzamos a contar desde el cero) es el d´onde empieza el primer
# n´umero de la serie que tiene 3 d´ıgitos. Encontrar la posici´on d´onde comienza el primer
# n´umero con 4 d´ıgitos.

#Realizar una funci´on que retorne la suma de todos los pares dentro de una serie de fibonacci, que est´e entre 0 y X
def fibonacci(n):
    a,b = 0 ,1
    c = 0
    for i in range (0,n):
        c +=1
        if i == 0:
            print (a)
        if len(str(b)) == 4:
            print ("tiene 4 digitos en la posicion: ",c ,"El numero: ",b)
            break
        print (b)
        a,b = b, a+b 
fibonacci(int(input("Introducir el rango de 0 X: ")))