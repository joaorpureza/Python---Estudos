# Tuplas são estruturas de dados imutáveis que armazenam vários itens em uma única variável.
# São definidas usando parênteses e são mais rápidas que listas em algumas operações.
# Criando uma tupla
carros = ("Fusca", "Civic", "Corolla")

# Acessando elementos
print(carros[0]) # Fusca

# Tentativas de modificação da tupla gera erro
# carros[0] = "Ferrari"

# Adicionando e removendo elementos, ou seja, criando uma nova tupla
carros = carros + ("Ferrari",)
print(carros)

# Slicing
# Permite acessar uma parte de uma sequência especificando um intervalo de índices
#Sintaxe: [início:fim:passo]. Início é o índice do primeiro elemento incluido, Fim é o do primeiro elemento excluido e o Passo é o incremento entre os índices.
print(carros[2:]) # ('Corolla', 'Ferrari')
