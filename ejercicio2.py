#Realizar una funci´on que retorne la suma de todos los pares dentro de una serie de fibonacci, que est´e entre 0 y X
def fibonacci(n):
    a,b = 0 ,1
    suma = 0
    for i in range (0,n):
        if i == 0:
            print (a)
        if b % 2 == 0 :
            suma +=b 
        print (b)
        a,b = b, a+b 
    return print("el resultado de los numeros pares es:",suma)
fibonacci(int(input("Introducir el rango de 0 a: ")))