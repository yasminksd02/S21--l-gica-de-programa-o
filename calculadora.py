def calculadora():
    # Exibe as opções de operação
    print("Escolha uma operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    # Recebe a escolha do usuário
    operacao = input("Digite o número correspondente à operação (1/2/3/4): ")

    # Verifica se a operação é válida
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida! Escolha uma opção válida.")
        return

    # Recebe os dois números do usuário
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números.")
        return

    # Realiza a operação escolhida
    if operacao == '1':
        resultado = num1 + num2
        simbolo = '+'
    elif operacao == '2':
        resultado = num1 - num2
        simbolo = '-'
    elif operacao == '3':
        resultado = num1 * num2
        simbolo = '*'
    elif operacao == '4':
        if num2 == 0:
            print("Erro! Divisão por zero não é permitida.")
            return
        resultado = num1 / num2
        simbolo = '/'

    # Exibe o resultado
    print(f"O resultado de {num1} {simbolo} {num2} é: {resultado}")

# Chama a função calculadora
calculadora()
