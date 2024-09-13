# Senha correta
senha_correta = "1234"

while True:
    # Solicita ao usuário que insira a senha
    senha = input("Digite a senha: ")
    
    # Verifica se a senha está correta
    if senha == senha_correta:
        print("Acesso permitido")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta")