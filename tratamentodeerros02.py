import math

try:
    x = int(input("digite a base: "))
    y = int(input("digite o expoente: "))
    result = pow(x, y)
    print(f"{x} elevado a {y} é igual a {result}")

except ValueError:
    print("entrada inválida. certifique-se de inserir números inteiros para a base e o expoente.")
except Exception as e:
    print(f"ocorreu um erro inesperado: {e}")

-------------------------------------------------------------------------------------------------------------------------

import math

while True:
    try:
        x = int(input("digite a base: "))
        y = int(input("digite o expoente: "))
        break
    except:
        print("erro! digite apenas números")

print(pow(x, y))
