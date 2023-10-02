class pessoa():

    nome = "pedro"
    idade = 23
    sexo = "M"
    salario = 7200

def imprime(p):
    print("nome: ", p.nome)
    print("idade: ", p.idade)
    print("salário: ", p.salario)

def retornaSalario(p):
    return p.salario
def calcIR(p):
    x = int(p.salario) * 27/100
    return x

def imprimePessoa(p):
    print(p)

p = pessoa
imprimePessoa(p)

p = pessoa(p)
p.imprime()
