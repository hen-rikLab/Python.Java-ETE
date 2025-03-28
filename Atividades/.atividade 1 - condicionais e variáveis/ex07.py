numero = int(input("Digite um número ímpar: "))

if numero % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    anterior = numero - 2
    proximo = numero + 2
    diferenca = (proximo ** 2) - (anterior ** 2)
    print(f"A diferença entre o quadrado de {proximo} e {anterior} é {diferenca}.")