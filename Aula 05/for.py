# Estrutura de repetição For (Para). Usada quando se sabe exatamente quantas vezes
# você deseja que o código faça o loop.

# Iterando sobre uma lista de números e imprimindo cada número
numeros = [2, 4, 6, 8, 10]
for numero in numeros:
    print(numero)
# Retornou os números da lista, mas já sabendo quantas vezes o loop se repetiria

# Usando o len no while para comparar:
numeros = [1, 2, 3, 4, 5]
indice = 0

while indice < len(numeros):
    print(numeros[indice])
    indice += 1
# Vemos que é necessário então usar uma variável indice para receber um incremento a cada loop.