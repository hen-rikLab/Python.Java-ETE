numero = int(input("Digite um número inteiro maior que 1: "))

if numero <= 1:
    print("O número deve ser maior que 1.")
else:
    primo = True
    for x in range(2, int(numero ** 0.5) + 1):
        if numero % x == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")