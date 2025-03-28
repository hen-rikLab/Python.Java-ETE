salario_inicial = float(input("Digite o salário inicial: "))
anos = int(input("Digite o número de anos: "))
aumento = float(input("Digite o percentual de aumento inicial (%): "))

salario_atual = salario_inicial

for ano in range(1, anos + 1):
    salario_atual += salario_atual * (aumento / 100)
    aumento *= 2

print(f"O salário após {anos} anos é R${salario_atual}")
