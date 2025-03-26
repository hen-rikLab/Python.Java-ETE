turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = 0

for x in range(turmas):
    alunos = int(input(f"Digite o número de alunos da turma {x + 1}: "))
    total_alunos += alunos
    if alunos > 40:
        print(f"Alerta: A turma {x + 1} tem mais de 40 alunos.")

media = total_alunos / turmas
print(f"A média de alunos por turma é {media}")
