produtos = []
valores = []

for i in range(3):
    produto = input("Digite o nome do produto {}: ".format(i + 1))
    valor = float(input("Digite o valor do produto {}: ".format(i + 1)))

    produtos.append(produto)
    valores.append(valor)

for produto, valor in zip(produtos, valores):
    print("O valor de {} é R${:.2f}".format(produto, valor)) # Não usar o float para valores monetários.
    # Usar a biblioteca decimal, porém nesse caso, usei a função format() e especifiquei
    # entre as chaves a formatação para exibir duas casas decimais.