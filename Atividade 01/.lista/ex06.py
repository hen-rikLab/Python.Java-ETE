numeros_primos = []
numero = 2

while len(numeros_primos) < 100:
    primo = True
    for x in range(2, int(numero ** 0.5) + 1):
        if numero % x == 0:
            primo = False
            break
    if primo:
        numeros_primos.append(numero)
    numero += 1

for primo in numeros_primos:
    print(primo)