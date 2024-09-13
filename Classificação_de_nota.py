# Função para calcular a média e classificar o aluno
def calcular_media_classificar(notas):
    media = sum(notas) / len(notas)
   #Se a média do aluno for menor que 7, ele está reprovado, caso contrario, aprovado 
    if media >= 7:
        return f"Média: {media:.2f} - Aprovado(a)"
    elif 5 <= media < 7:
        return f"Média: {media:.2f} - Recuperação"
    else:
        return f"Média: {media:.2f} - Reprovado(a)"

while True:
    nome = input("\nDigite o nome do aluno: ")
    notas = []

    # Coleta a nota de 3 alunos
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota de {nome}: "))
        notas.append(nota)

    # Exibe a classificação do aluno
    resultado = calcular_media_classificar(notas)
    print(f"Aluno: {nome} - {resultado}")

    # Verifica se o usuario deseja continuar
    continuar = input("\nDeseja inserir notas de outro aluno? (S/N): ").strip().lower()
    if continuar != 's':
        print("\nFinalizando o programa.")
        break
