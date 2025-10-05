# Lê a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializa as variáveis
soma_idades = 0
contador = 0

# Usa o while para ler as idades
while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

# Calcula a média
media = soma_idades / N

# Exibe o resultado
print(f"A média das idades é: {media:.2f}")
