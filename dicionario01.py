d = {12: "manuel", 13: "pedro", 14: "izabela"}
print(d)
d.copy()
print(d)
print(d.keys())

for i in range(len(d)):
    print(i)
for i in d:
    print(i)

print(d.values())

d1 = {45: "joaquim"}
d.update(d1)
print(d)

print(d.get(12))
d[12] = "kkkk"
print(d.get(12))
print(d)
d.popitem()
print(d)


notas = { "João"  : 9,
          "Maria" : 10,
          "José"  : 4}

nome = input("digite o nome do aluno: ")
nota = float(input("digite sua nota: "))
print("antigo dicionário--------", notas)

if notas.get(nome):
    print("Já existe o aluno ", nome)
else:
    d[nome] = nome
print("novo dicionário------------")
print(d)

print(d.keys())

print(d.values())
