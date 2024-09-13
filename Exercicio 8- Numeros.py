# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Imprime números pares
print("Números pares:")
for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)

# Imprime números ímpares
print("Números ímpares:")
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)
