# Pedir números ao usuário até que seja digitado um número > 0 ou  <= 100
numero = 1

while numero > 0 and numero <= 100:
    numero = int(input("Digite um número maior que 0 e menor ou igual a 100: "))

# Interessante notar como os pedidos de input aqui estão dentro do laço.