notas = []
pesos1 = [2, 2, 3]
pesos2 = [1, 2, 2]

for x in range (3):
    while True:
        try:
            nota = float(input(f"Digite a {x + 1}ª nota: "))
            notas.append(nota)
            break

        except ValueError:
            print("Insira todas as notas para poder prosseguir.")

media_aritimetica = sum(notas) / len(notas)

media_ponderada1 = (notas[0] * pesos1[0] + notas[1] * pesos1[1] + notas[2] * pesos1[2]) / sum(pesos1)
media_ponderada2 = (notas[0] * pesos2[0] + notas[1] * pesos2[1] + notas[2] * pesos2[2]) / sum(pesos2)

print(f"Média aritmética das notas: {media_aritimetica}")
print(f"Média ponderada com pesos({", ".join(map(str, pesos1))}) das notas: {media_ponderada1}")
print(f"Média ponderada com pesos({", ".join(map(str, pesos2))}) das notas: {media_ponderada2}")


'''
jeito fofo:
    media_ponderada1 = sum(nota * peso for nota, peso in zip(notas, pesos1)) / sum(pesos1)
    media_ponderada2 = sum(nota * peso for nota, peso in zip(notas, pesos2)) / sum(pesos2)

    print(f"Média aritmética das notas: {media_aritimetica:.2f}")
    print(f"Média ponderada com pesos({', '.join(map(str, pesos1))}): {media_ponderada1:.2f}")
    print(f"Média ponderada com pesos({', '.join(map(str, pesos2))}): {media_ponderada2:.2f}")
'''