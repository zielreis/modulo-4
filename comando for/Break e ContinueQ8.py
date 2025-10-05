#Vamos fazer uma calculadora que aceita
#expressões aritméticas de qualquer tamanho 
#até que o usuário digite a palavra "Fim".
#Sua calculadora executa
#Comando for Q4apenas as operações "+", "-".


# Calculadora que aceita apenas "+" e "-" até o usuário digitar "Fim"

resultado = 0
operador = "+"  # operador inicial é + para somar o primeiro número

while True:
    entrada = input("Digite um número ou operador (+, -) ou 'Fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    # verifica se é um operador
    if entrada in "+-":
        operador = entrada
        continue  # vai para a próxima entrada

    # senão, é um número
    numero = int(entrada)

    if operador == "+":
        resultado += numero
    elif operador == "-":
        resultado -= numero

print("Resultado:", resultado)
