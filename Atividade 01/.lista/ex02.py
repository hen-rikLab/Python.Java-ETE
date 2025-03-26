segundos = int(input("Digite um valor em segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")