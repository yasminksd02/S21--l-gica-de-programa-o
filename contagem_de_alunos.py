# Variaveis
alunos = []
notas = []
soma_notas = 0
qtd_alunos = 10

# Faz input dos nomes e notas dos alunos
for i in range(qtd_alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))
    soma_notas += nota

# Calculando a média da turma
media_turma = soma_notas / qtd_alunos
print(f"\nA média da turma é: {media_turma:.2f}\n")

# Classifica os alunos como aprovados e reprovados
for aluno, nota in alunos:
    if nota >= 7:
        print(f"{aluno} está Aprovado(a) com nota {nota:.2f}")
    else:
        print(f"{aluno} está Reprovado(a) com nota {nota:.2f}")
