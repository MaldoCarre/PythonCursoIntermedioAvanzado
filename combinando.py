# de dos listas convinar los valores sin repetir

# primera forma sin list list comprehensions
list1 = [1,2,3]
list2 = [3,4,5]
result = []
for i in list1:
    for l in list2:
        if i != l:
            result.append((i,l))
            result.append((l,i))
        else:
            pass    
print(result)

#usando list comprehensions
lista = [1,2,3]
listb = [3,4,5]
resultado=[((i,l),(l,i))for i in lista for l in listb if i != l]
print(resultado)