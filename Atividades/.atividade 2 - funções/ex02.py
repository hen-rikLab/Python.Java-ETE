import json
import os

diretorio_raiz = os.path.dirname(__file__)
diretorio = os.path.join(diretorio_raiz, 'dados/estoque.json')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_estoque():
    if not os.path.exists('dados'):
        os.makedirs('dados')
    try:
        with open(diretorio, 'r') as f:
            return json.load(f)
    except:
        return []

def salvar_estoque(estoque):
    with open(diretorio, 'w') as f:
        json.dump(estoque, f, indent=2)

def adicionar_produto(estoque):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso!")

def listar_produtos(estoque):
    total = 0
    for p in estoque:
        valor_produto = p['quantidade'] * p['preco']
        total += valor_produto
        print(f"{p['nome']} - {p['quantidade']} unidades - R${p['preco']:.2f} cada (Total: R${valor_produto:.2f})")
    print(f"\nValor total do estoque: R${total:.2f}")

def main():
    estoque = carregar_estoque()
    while True:
        print("\n1. Adicionar produto\n2. Listar produtos\n0. Sair")
        op = input("Opção: ")
        limpar_terminal()

        if op == "1":
            adicionar_produto(estoque)
        elif op == "2":
            listar_produtos(estoque)
            limpar_terminal()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
        limpar_terminal()
    salvar_estoque(estoque)

main()