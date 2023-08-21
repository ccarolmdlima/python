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
