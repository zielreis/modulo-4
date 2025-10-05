#Escreva um programa que lê uma quantidade
# indefinida de valores e informa o produto dos valores positivos digitados. A
# leitura é encerrada quando o usuário digitar o valor 0 (zero).


# estado inicial

produto=1

while True:
    n = int(input())
    if n==0: break
    
    if n <0: continue
    
    produto = produto * n
    
    
    print(f" o produto dos positivos:{produto}")


