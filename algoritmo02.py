#dada a lista abaixo
l = [5,4,3,2,8,7,4,9] #int
#pede-se
#1) imprima os 3 últimos elementos
#2) ordene a em ordem crescente e decrescente
#3) insira um elemento no início da l

print(len(l))
print(l[5: ])
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.insert(0, 11)
print(l)
