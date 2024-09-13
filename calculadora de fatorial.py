def calcular_fatorial():
    # Solicita um número inteiro do usuário
    try:
        numero = int(input("Digite um número inteiro positivo: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        return

    # Verifica se o número é positivo
    if numero < 0:
        print("Número inválido! O número deve ser positivo.")
        return

    # Calcula o fatorial usando uma estrutura de repetição
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")

# Chama a função para calcular o fatorial
calcular_fatorial()
