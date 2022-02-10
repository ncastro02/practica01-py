lista1=[1,2,3,4,5]
print(lista1)
for number in lista1:
    print(number)

lista1.append(24)
for number in lista1:
    print(number)

lista1.remove(5)
print(lista1)

lista1.insert(1,86)
print(lista1)

lista1.pop()
print(lista1)

lista1.reverse()
print(lista1)

lista1.sort()
print(lista1)

lista1.clear()
print(lista1)

lista2=[1,5,3,[8,78,2]]
for x in range(len(lista2)):
    if(x==3):
        for y in range(len(lista2[x])):
            print(lista2[x][y])
    else:
        print(lista2[x])

