import json
import os

diretorio_raiz = os.path.dirname(__file__)
diretorio = os.path.join(diretorio_raiz, 'dados/contatos.json')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_contatos():
    try:
        with open(diretorio, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_contatos(contatos):
    with open(diretorio, 'w') as f:
        json.dump(contatos, f, indent=2)

def adicionar_contato(contatos):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(contato)
    salvar_contatos(contatos)
    print(f"Contato {nome} adicionado com sucesso!")

def buscar_contato(contatos):
    nome_busca = input("Digite o nome para buscar: ").strip().lower()
    encontrados = [c for c in contatos if nome_busca in c['nome'].lower()]
    
    if encontrados:
        print("\nContatos encontrados:")
        for contato in encontrados:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato encontrado.")

def listar_contatos(contatos):
    if contatos:
        print("\nLista de Contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato cadastrado.")

def main():
    contatos = carregar_contatos()

    while True:
        print("\n=== Gerenciador de Contatos ===\n 1. Adicionar novo contato \n 2. Buscar contato pelo nome \n 3. Listar todos os contatos \n 0. Sair") 
        opcao = input("Escolha uma opção: ")
        limpar_terminal()

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            buscar_contato(contatos)
        elif opcao == '3':
            listar_contatos(contatos)
        elif opcao == '0':
            print("Saindo do gerenciador...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        passe = input("Pressione Enter para continuar...")
        limpar_terminal()

main()