Aluno1 = ("João", 11, "5º Ano")
Aluno2 = ("Maria", 13, "7º Ano")
Aluno3 = ("Pedro", 14, "8º Ano")

notas_aluno1 = (8.5, 7.0, 9.0, 6.5)
notas_aluno2 = (9.0, 8.5, 7.5, 10.0)
notas_aluno3 = (6.0, 7.5, 8.0, 9.0)

nome1, idade1, turma1 = Aluno1
print(f"Nome: {nome1}, Idade: {idade1}, Turma: {turma1}")

nome2, idade2, turma2 = Aluno2
print(f"Nome: {nome2}, Idade: {idade2}, Turma: {turma2}")

nome3, idade3, turma3 = Aluno3
print(f"Nome: {nome3}, Idade: {idade3}, Turma: {turma3}")

nota1_1, nota1_2, nota1_3, nota1_4 = notas_aluno1
print(f"Notas de {nome1}: {nota1_1}, {nota1_2}, {nota1_3}, {nota1_4}")

nota2_1, nota2_2, nota2_3, nota2_4 = notas_aluno2
print(f"Notas de {nome2}: {nota2_1}, {nota2_2}, {nota2_3}, {nota2_4}")

nota3_1, nota3_2, nota3_3, nota3_4 = notas_aluno3
print(f"Notas de {nome3}: {nota3_1}, {nota3_2}, {nota3_3}, {nota3_4}")

print(min(notas_aluno1)) # Menor nota do Aluno1

print(max(notas_aluno2)) # Maior nota do Aluno2

print(sum(notas_aluno3)) # Soma das notas do Aluno3