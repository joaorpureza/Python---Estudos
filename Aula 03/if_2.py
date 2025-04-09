# Multiplos If's
# Solicitando a nota de uma aluno
nota = float(input("Digite a nota do aluno: "))

# Situação do aluno
if nota >= 9.0:
    print("Conceito A - Excelente")
if nota >= 7.0 and nota < 9.0:
    print("Conceito B - Bom")
if nota >= 5.0 and nota < 7.0:
    print("Conceito C - Regular")
if nota < 5:
    print("Conceito D - Insuficiente")