def main():
    # Inicia um loop infinito para permitir múltiplas entradas do usuário
    while True:
        # Solicita ao usuário a idade ou o comando para sair
        idade_input = input("Digite a idade da pessoa (ou 'sair' para terminar): ")
        
        # Verifica se o usuário digitou 'sair' para encerrar o programa
        if idade_input.lower() == 'sair':
            # Sai do loop e encerra o programa
            break
        
        try:
            # Tenta converter a entrada para um número inteiro
            idade = int(idade_input)
        except ValueError:
            # Se a conversão falhar, exibe uma mensagem de erro e continua o loop
            print("Por favor, insira um número válido.")
            continue
        
        # Verifica a faixa etária da pessoa com base na idade fornecida
        if idade < 18:
            # Se a idade é menor que 18, classifica como "Menor de idade"
            print("Menor de idade")
        elif idade < 60:
            # Se a idade é entre 18 e 59, classifica como "Adulto"
            print("Adulto")
        else:
            # Se a idade é 60 ou mais, classifica como "Idoso"
            print("Idoso")

# Verifica se o script está sendo executado diretamente e, se sim, chama a função main
if __name__ == "__main__":
    main()
