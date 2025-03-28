dias = int(input("Digite o número de dias: "))
quilometros = float(input("Digite os quilômetros rodados: "))

custo_dia = 90
taxa_km = 12
limite_km = 100

custo_basico = dias * custo_dia
quilometros_extras = quilometros - limite_km
custo_extra = quilometros_extras * taxa_km
valor_total = custo_basico + custo_extra

print(f"O valor total a ser pago é: R${valor_total}")