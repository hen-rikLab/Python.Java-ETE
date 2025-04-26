import json
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_reservas():
    if not os.path.exists('dados'):
        os.makedirs('dados')
    try:
        with open('dados/reservas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [[0 for _ in range(5)] for _ in range(5)] 

def salvar_reservas(reservas):
    with open('dados/reservas.json', 'w') as f:
        json.dump(reservas, f, indent=2)

def exibir_mapa(reservas):
    print("\nMapa de Assentos:")
    for i, linha in enumerate(reservas):
        linha_str = " ".join(['🟩' if assento == 0 else '🟥' for assento in linha])
        print(f"Linha {i+1}: {linha_str}")

def reservar_assento(reservas):
    exibir_mapa(reservas)
    linha = int(input("Escolha a linha (1-5): ")) - 1
    coluna = int(input("Escolha a coluna (1-5): ")) - 1
    if 0 <= linha < 5 and 0 <= coluna < 5:
        if reservas[linha][coluna] == 0:
            reservas[linha][coluna] = 1
            print("Assento reservado com sucesso!")
        else:
            print("Este assento já está reservado.")
    else:
        print("Assento inválido. Tente novamente.")

def cancelar_reserva(reservas):
    exibir_mapa(reservas)
    linha = int(input("Escolha a linha (1-5) para cancelar: ")) - 1
    coluna = int(input("Escolha a coluna (1-5) para cancelar: ")) - 1
    if 0 <= linha < 5 and 0 <= coluna < 5:
        if reservas[linha][coluna] == 1:
            reservas[linha][coluna] = 0
            print("Reserva cancelada com sucesso!")
        else:
            print("Este assento não está reservado.")
    else:
        print("Assento inválido. Tente novamente.")

def main():
    reservas = carregar_reservas()
    
    while True:
        print("\n1. Reservar um assento\n2. Cancelar uma reserva\n3. Exibir mapa de assentos\n0. Sair")
        op = input("Escolha uma opção: ")
        limpar_terminal()

        if op == "1":
            reservar_assento(reservas)
        elif op == "2":
            cancelar_reserva(reservas)
        elif op == "3":
            exibir_mapa(reservas)
        elif op == "0":
            break
        else:
            print("Opção inválida.")
        
        salvar_reservas(reservas)
        passe = input("Pressione Enter para continuar...")
        limpar_terminal()

main()