#Você vai criar um sistema que registra os resultados dos jogos do Atlético MG 
# ao longo de um campeonato. Seu sistema vai receber os resultados de todos os
# jogos do Galo, e deve calcular a pontuação do time sabendo que vitórias valem 3 pontos,
# empates 1 ponto e derrotas 0 pontos.

#Entrada:
#A primeira linha de entrada é um inteiro N com a quantidade jogos do galo.
# Para cada jogo você deve ler 2 inteiros, o primeiro com a quantidade de gols do galo 
# e o segundo com a quantidade de gols do time oponente.

#Saída:
#Apresente a soma de vitórias, empates e derrotas do galo, 
# junto com o cálculo da pontuação total.

n =int(input("numeros de jogos"))

soma_vitorias, soma_empates, soma_derrotas=0,0,0



for jogo in range (n):
    gols_galo = int(input(f"digite gols do galo no jogo{jogo}:"))
    gols_op= int(input(f"digite gols do oponente no jogo {jogo}:"))
    
    if gols_galo> gols_op:
        soma_vitorias+=1
    elif gols_galo<gols_op:
     soma_derrotas+=1
    else:# nao é maior , nao é mennor
        soma_empates+=1
    
    print("total de vitorias",soma_vitorias)
    print ("total de empates ",soma_empates)
    print("total de derrotas",soma_derrotas)
    print("pontuação",3*soma_vitorias+soma_empates)