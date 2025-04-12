# Manipulação dinâmica de listas
# Criando um array de tamanho 5
numeros = [0] * 5
 # Solicitando 5 números inteiros ao usuário
for i in range(5):
        numeros[i] = int(input("Digite o {}º número inteiro: ".format(i + 1)))
# Como visto na aula anterior, a .format() insere valores na string e substitui os marcadores {}
# pelos valores fornecidos, trazendo dinamismo.

# Imprimindo cada número com sua posição na lista
for i, numero in enumerate(numeros):
        print("O número {} está na posição {} da lista.".format(numero, i))
# A primeira chave {} é preenchida por "numero" e a segunda por i.