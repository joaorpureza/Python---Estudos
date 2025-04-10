# Algumas operações usando o for
# Calculando a soma de uma sequência de números
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero # soma = soma + numero

print("A soma dos números é:", soma)
# O loop percorre cada elemento da lista e incrementa o valor na variável soma.
# Se fosse adaptar para o portugol seria soma <- soma + numero.
# Então o loop vai: 0 + 1 = 1/ 1 + 2 = 3/ 3 + 3 = 6/ 6 + 4 = 10/ 10 + 5 = 15 