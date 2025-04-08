# Declarando variável do tipo inteiro (int)
numero: int

# Input do usuário para inserir um número inteiro
numero = int(input("Digite um número inteiro: "))
# Aqui foi dito explicitamente que o input pedido seria um inteiro.
# Sem usar a função interna, o código poderia aceitar qualquer tipo de entrada e tentaria converter a variável para o tipo correto.

# Usando o type() para verificar
print(type(numero))
print(numero)