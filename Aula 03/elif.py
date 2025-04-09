# Elif, ou Else If, serve para não precisar aninhar vários If's nas condições.
# Solicitar os anos de experiência de um profissional
anos_experiencia = int(input("Digite quantos anos de experiência o profissional possui: "))

#Verificar a classificação do profissional 
if anos_experiencia < 5:
    print("Profissional em início de carreira - Júnior")
elif anos_experiencia >= 5 and anos_experiencia < 10:
    print("Profissiona Pleno")
elif anos_experiencia >= 10 and anos_experiencia < 15:
    print("Profissional Sênior")
else:
    print("Profissional Master")

#Else é o senão.