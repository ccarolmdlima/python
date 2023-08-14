nota = []
nome = []

def lenotanome():
    x = int(input("digite a quantidade de alunos: "))
    for i in range(x):
        print("aluno {}" .format(i))
        n = float(input("digite a nota do aluno: "))
        m = input("digite o nome do aluno: ")
        nota.append(n)
        nome.append(m)

def avalianota():
    for i in range(len(nome)):
        if nota[i] >= 9.0 and nota[i] <= 10:
            print("o aluno {} tem conceito A e nota {}" .format(nome[i]
            ,nota[i]))
        if nota[i] < 9.0 and nota[i] >= 8.0:
            print("o aluno {} tem conceito B e nota {}" .format(nome[i]
            ,nota[i]))
        if nota[i] >= 7.0 and nota[i] < 8.0:
            print("o aluno {} tem conceito C e nota {}" .format(nome[i]
            ,nota[i]))

print("o programa começa aqui")
lenotanome()
print("meio do programa")
avalianota()
print("fim do programa")
