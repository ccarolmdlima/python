x = int(input("digite um número para x: "))
y = int(input("digite um número para y: "))

try:
    z = x/y
except:
    print("não pode fazer divisão por zero!")
print(z)
