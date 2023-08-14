nota = []
nome = []

def lenotanome():
    try:
        x = int(input("Digite a quantidade de alunos: "))
        for i in range(x):
            print("Aluno {}".format(i))
            while True:
                try:
                    n = float(input("Digite a nota do aluno: "))
                    if 0 <= n <= 10:
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Digite um valor numérico válido para a nota.")
                
            m = input("Digite o nome do aluno: ")
            nota.append(n)
            nome.append(m)
    except ValueError:
        print("Digite um valor numérico válido para a quantidade de alunos.")

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
