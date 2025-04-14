# Funções com tuplas realizam operações como contagem, cálculos de comprimento, soma etc.
# Ótimo para tratar dados de Excel, facilitando o acesso e manipulação de bibliotecas como pandas ou openpyxl
tupla = (1, 2, 3, 4, 5)
# Contando a ocorrência do número 2
print(tupla.count(2)) #Saída: 2

# Encontrando o índice da primeira ocorrência do número 2
print(tupla.index(2)) # Saída: 1

# Obtendo o comprimento da tupla
print(len(tupla)) # Saída: 6

# Encontrando o maior elemento da tupla
print(max(tupla)) # Saída: 5

# Encontrando o menor elemento da tupla
print(min(tupla)) # Saída: 1

# Calculando a soma de todos os elementos da tupla
print(sum(tupla)) # Saída: 17

# Verificando se algum elemento é verdadeiro
print(any(tupla)) # Saída: True(pois há números diferentes de zero)

#Verificando se todos os elementos são verdadeiros
print(all(tupla)) # Saída: True(pois todos são diferentes de zero)

# Ordenando a tupla (retorna uma lista)
print(sorted(tupla)) # Saída: [1, 2, 3, 4, 5]

# Revertendo a tupla (retorna um iterador)
print(list(reversed(tupla))) # Saída: [5, 4, 2, 3, 2, 1]
# Percorre uma sequência de elementos, um de cada vez, gerando cada elemento sob demanda.