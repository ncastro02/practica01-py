registroNombre=("Jesús")

...
#for value in registroNombre:
    #print(value)
...

#print(registroNombre[0])

lis=[1,2,3]
for v in range(len(lis)):
    lis.insert(1,lis[v])
#print(lis)

lis=[3,1,-2]
#print(lis[lis[-1]])

i=0
while i <=5:
    i +=1
    if i % 2 == 0:
        break
    #print("*")

vals=[0,1,2]
vals.insert(0,1)
del vals[1]
#print(vals)

t=[[3-i for i in range(3)]for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
#print(s)

