# Lê a quantidade de experimentos
n = int(input("Digite a quantidade de experimentos: "))

# Inicializa contadores
cont = 0
total = 0
soma_sapos = 0
soma_ratos = 0
soma_coelhos = 0

# Loop principal
while cont < n:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo = input("Digite o tipo (S, R ou C): ").upper()
    
    total += quantia  # soma total de cobaias

    # Atualiza de acordo com o tipo
    if tipo == 'S':
        soma_sapos += quantia
    elif tipo == 'R':
        soma_ratos += quantia
    elif tipo == 'C':
        soma_coelhos += quantia
    else:
        print("Tipo inválido! Use apenas S, R ou C.")
        cont -= 1  # repete a leitura se tipo inválido

    cont += 1

# Calcula percentuais
perc_sapos = (soma_sapos / total) * 100
perc_ratos = (soma_ratos / total) * 100
perc_coelhos = (soma_coelhos / total) * 100

# Mostra resultados
print("\n--- RELATÓRIO FINAL ---")
print("Total de cobaias:", total)
print("Total de sapos:", soma_sapos)
print("Total de ratos:", soma_ratos)
print("Total de coelhos:", soma_coelhos)
print(f"Percentual de sapos: {perc_sapos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
