mercadoria = float(input("Qua o valor total da mercadoria? "))

if mercadoria > 500:
    taxa = (mercadoria * 0.5)
    print("O valor se aplica nas condições de imposto.")
    print(f"Taxa de R${taxa} aplicada.")
    print(f"Valor total a se pagar: R${taxa + mercadoria}")

else:
    print("O valor não se aplicas às condições de imposto.")
    print(f"Valor total a se pagar: R${mercadoria}")