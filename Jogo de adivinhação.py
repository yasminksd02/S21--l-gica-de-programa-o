import random  # Importa o módulo random para gerar números aleatórios

def jogo_adivinhacao():  # Define a função principal do jogo
    numero_secreto = random.randint(1, 50)  # Gera um número aleatório entre 1 e 50 e armazena em 'numero_secreto'
    tentativas = 5  # Define o número máximo de tentativas que o usuário tem

    print("Bem-vindo ao jogo de adivinhação!")  # Exibe uma mensagem de boas-vindas
    print("Eu escolhi um número entre 1 e 50. Tente adivinhar qual é!")  # Informa ao usuário o objetivo do jogo

    while tentativas > 0:  # Loop que continua enquanto o usuário tiver tentativas restantes
        palpite = int(input("Digite seu palpite: "))  # Solicita ao usuário um palpite e converte para um inteiro
        
        if palpite < numero_secreto:  # Verifica se o palpite é menor que o número secreto
            print("O número é maior que o seu palpite.")  # Informa ao usuário que o número secreto é maior
        elif palpite > numero_secreto:  # Verifica se o palpite é maior que o número secreto
            print("O número é menor que o seu palpite.")  # Informa ao usuário que o número secreto é menor
        else:  # Caso o palpite seja igual ao número secreto
            print(f"Parabéns! Você adivinhou o número {numero_secreto}!")  # Informa ao usuário que ele acertou o número
            return  # Encerra a função e o jogo
        
        tentativas -= 1  # Decrementa o número de tentativas restantes
        print(f"Você tem {tentativas} tentativas restantes.")  # Informa ao usuário quantas tentativas ainda tem

    print(f"Game over! O número era {numero_secreto}.")  # Informa ao usuário o número secreto após todas as tentativas

# Executa o jogo chamando a função
jogo_adivinhacao()
