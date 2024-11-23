alunos = int(input("Digite o número de alunos: "))

medias_turma = []

for i in range(1, alunos + 1):
    print(f"Aluno {i}:")
    nome = input("Digite o nome do aluno: ")
    
    notas = []
    for x in range(1, 4):
        nota = float(input(f"Digite a nota {x}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias_turma.append(media)
    
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    
    print(f"\nResultados do aluno {nome}:")
    print(f"Notas: {notas}")
    print(f"Média: {media}")
    print(f"Status: {status}")

media_geral = sum(medias_turma) / alunos

print(f"Média geral da turma: {media_geral}")
