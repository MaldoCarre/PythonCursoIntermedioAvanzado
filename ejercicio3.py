# La suma de los cuadrados de los primeros 10 n´umeros naturales es:
# 1
# 2 + 22 + 32 + ... + +102 = 385 (1)
# El cuadrado de la suma de los primeros 10 n´umeros naturales es:
# (1 + 2 + 3 + ... + 10)2 = 3025 (2)
# La diferencia entre la suma de los cuadrados de los primeros 10 n´umeros naturales y
# el cuadrado de las sumas es: 3025 − 385 = 2640
# Realizar una funci´on que devuelva la diferencia de la suma de los cuadrados de los
# primeros X n´umeros naturales y el cuadrado de la suma.
def difcuad ():
    suma = 0 
    resultado = 0 
    n = int(input("Introducir el rango X :")) 
    for i in range (1,n+1): suma +=i**2
    for i in range(1,n+1):resultado += i
    resultado = resultado**2
    diferencia=resultado-suma
    return print("El resultado final es:",diferencia)
difcuad()
