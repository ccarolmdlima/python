nota = []
nome = []

def lenotanome():
    x = int(input("Digite a quantidade de alunos: "))
    for i in range(x):
        print("Aluno {}".format(i))
        n = float(input("Digite a nota do aluno: "))
        m = input("Digite o nome do aluno: ")
        nota.append(n)
        nome.append(m)

def avalianota():
    for i in range(len(nome)):
        if 9.0 <= nota[i] <= 10:
            print("O aluno {} tem conceito A e nota {}".format(nome[i], nota[i]))
        elif 8.0 <= nota[i] < 9.0:
            print("O aluno {} tem conceito B e nota {}".format(nome[i], nota[i]))
        elif 7.0 <= nota[i] < 8.0:
            print("O aluno {} tem conceito C e nota {}".format(nome[i], nota[i]))

print("O programa começa aqui")
lenotanome()
print("Meio do programa")
avalianota()
print("Fim do programa")
print("Nomes:", nome)
print("Notas:", nota)
