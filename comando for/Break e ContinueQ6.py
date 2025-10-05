#Escreva um programa que lê uma quantidade
# indefinida de valores e informa o maior
# e o menor valor digitados.
# A leitura é encerrada quando o usuário
# digitar o valor 0 (zero).

n = int(input())


# estado inicial de variaveis
maior=float('-inf')
menor=float('-inf')

while True:
    n= int(input())
    if n==0:break
    
    if n > maior:
        maior= n
 
    if n <menor:
        menor=n
    
    #sainda de dados
    print(f"o maior valor é(maior)")
    print(f"o menor valor é (menor)")
    