# Solicitar dados enquanto o usuário digitar "sim".
resposta = input("Deseja continuar? (digite 'sim' para continuar): ")
# Python é case-sensitve, distingue entre maiúsculas e minúsculas em comparações e identificadores.
# É utilizada a função lower(), normalizando strings e mantendo todas as letras minúsculas, para tornar o código mais flexível.
# Mas, é importante manter o case-sentive ativo em casos de senhas, por exemplo.

while resposta.lower() == "sim":
    resposta = input("Deseja continuar? (digite 'sim' para continuar): ")

# O lower() aqui tornou todas as letras da string minúsculas. No teste, o código só parou quando foi digitado algo diferente de 'sim'. Sendo maiúscula ou minúscula.