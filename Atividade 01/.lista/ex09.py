numeros = []

for x in range(3):
    numero = float(input(f"Digite o número {x + 1}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")