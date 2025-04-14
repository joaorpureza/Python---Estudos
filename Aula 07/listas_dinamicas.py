# Listas dinâmicas podem ser mudadas durante a execução dos programas
lista_de_carros = []

quantidade = int(input("Quantos carros você deseja adicionar à lista?"))

for i in range(quantidade): #Adiciona carros à lista de acordo com a quantidade necessária
    carro = input(f"Digite o nome do carro {i}: ") # fstring permite a inserção de números na string com as {}
    lista_de_carros.append(carro)

print("Lista de carros criada:", lista_de_carros)

# Uma lista dinâmica oferece maior flexibilidade e é útil quando o número de itens é desconhecido ou varia.
# Uso do For porque o programa já entende quantas vezes irá rodar o loop.

# Loop para exibir a posição e o carro na lista
for index, carro in enumerate(lista_de_carros):
    print(f"Na posição {index} está o carro: {carro}")

# Solicita o índice para excluir
indice_exclusao = int(input(f"Digite o índice de 0 a {len(lista_de_carros) - 1} para excluir um carro: "))
# Verifica se o índice está dentro do intervalo válido
if 0 <= indice_exclusao < len(lista_de_carros):
    carro_removido = lista_de_carros.pop(indice_exclusao)
    print(f"Carro '{carro_removido}' foi removido da lista.")
else:
    print("Erro: índice inválido.")