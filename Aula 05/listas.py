# Estudo das listas em Python. Em outras linguagens é o array.
# Mas em Python, as listas são mais flexíveis

# Criando uma lista numérica
numeros = [1, 3, 5, 7, 9]
# Cada um deles representa um índice, começando do 0. Então o num 1 está no índice 0, e assim por diante.
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])
# Para pegar um elemento da lista, usamos colchetes []
# Se quisermos pegar o último elemento da lista usamos [-1], penúltimo [-2], e assim por diante.

# Modificando um elemento da lista
numeros[0] = 10
print("Lista após modificação:", numeros)
# Índice 0 da lista números recebe o novo valor 10

# Adicionando um novo elemento a lista
numeros.append(6)
print("Lista após adição:", numeros)
# Usar o .append() para realizar a tarefa

# Removendo o último elemento da lista
ultimo_elemento = numeros.pop()
print("Elemento removido:", ultimo_elemento)
print("Lista após a remoção:", numeros)
# Usar o .pop() para realizar a tarefa

# Removendo um elemento específico da lista
numeros.remove(5) # Remove o número 5 da lista
print("Lista após a remoção:", numeros)
# Usar o .remove() para realizar a tarefa

# Removendo um elemento específico pelo índice
print("Elemento que será removido:", numeros[2])
del numeros[2] # Remove o elemento de índice 2 da lista
print("Lista após remoção:", numeros)
# Usar o del para realizar a tarefa