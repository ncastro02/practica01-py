import math

x=float(input('Ingresa x:'))
y=math.sqrt(x)

print("La raiz cuadrada de",x,"es igual a",y)

first_number=int(input("Ingresa el primer numero: "))
second_number=int(input("Ingresa el segundo numero: "))

try:
    print(first_number/second_number)
except:
    print("Esta operacion no puede ser realizada")

print("FIN.")