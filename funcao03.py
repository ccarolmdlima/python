import math

def pot(x, y):
    i = y 
    z = 1
    while i > 0:
        i = i - 1
        z = z * x
    return z

x = int(input("digite a base: "))
y = int(input("digite o expoente: "))

z = pot(x, y)
print(z)

print(math.sqrt(9))

---------------------------------------------------------------------------------------------------

#função que retorna o valor da potência

import math

def pot(x, y):
    i = y 
    z = 1
    while i > 0:
        i = i - 1
        z = z * x
    return z

def entrada():
   try:
        x = int(input("digite a base: "))
        y = int(input("digite o expoente: "))
   except:
        print("erro! digite apenas números")

entrada()

print(pow(x, y))
print(math.sqrt(9))
