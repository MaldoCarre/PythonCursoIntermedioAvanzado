# Escribir una función que elimine números repetidos de una lista.
def borrarep():
    listaA = [1, 3, 5, 6, 3, 5, 6, 1,6,6,6,6,5,5,5,5,1,1,1,2,3,4,5,6,7,8,3,3,3,3,4,4,4,4,4,4,4] 
    res= []
    for i in listaA:
        if i not in res:
            res.append(i)
    return print(res)
borrarep()