#nota >= 9 - A
#nota = 8 - B
#nota = 7 - C

n1 = 9.5; n2 = 8.5; n3 = 7.5
a1 = "pedro"; a2 = "felipe"; a3 = "joaquim"
if n1 >= 9.0:
    print("conceito A para o aluno: ", a1)
if n2 >= 8.0 and n2 < 9.0:
    print("conceito B para o aluno: ", a2)
if n3 >= 7.0 and n3 < 8.0:
    print("conceito C para o aluno: ", n3)

#usando for
n = [9.5, 8.5, 7.5]
a = ['pedro', 'felipe', 'joaquim']

for i in range(len(n)):
    if n[i] >= 9.0:
        print('conceito A para o aluno: ', a[i])
    if n[i] >= 8.0 and n[i] < 9.0:
        print('conceito B para o aluno: ', a[i])
    if n[i] >= 7.0 and n[i] < 8.0:
        print("conceito C para o aluno: ", n[i])
