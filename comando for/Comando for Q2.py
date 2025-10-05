# Programa que calcula a soma de 1 até n

n = int(input("Digite um número: "))

soma = 0
for i in range(1, n + 1):
    soma += i  # acumula a soma

print(f"A soma dos números de 1 a {n} é {soma}")
