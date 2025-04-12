# Iteração em duas listas ao mesmo tempo
# Uma com zip(), outra com range() e outra com enumerate()
produtos = ["PC Gamer", "Xbox Series", "PlayStation 5", "Nintendo Switch", "Notebook Gamer"]
valores = [8000, 3000, 4500, 2500, 6000]

# Usando zip().
for produto, valor in zip(produtos, valores):
    print("O valor de {} é R${}".format(produto, valor)) # Combina duas ou mais listas
# O for percorre as listas ao mesmo tempo, se uma for maior que a outra, os elementos extras são ignorados.
# É uma maneira prática de percorrer listas ao mesmo tempo.

# Usando range().
for i in range(len(produtos)):
    print("O valor de {} é R${}".format(produtos[i], valores[i]))
# Usando len() também para acessar os elementos da lista pelo índice.

# Usando enumerate().
for i, produto in enumerate(produtos):
    print("O valor de {} é RS {}".format(produto, valores[i]))
# Percorre a lista de produtos, fornecendo índice e valor.

# Se o tamanho de "produtos" for maior que "valores", a iteração ocorre sobre as duas,
# mas vai retornar o erro "list index out of range" no range() e no enumerate()