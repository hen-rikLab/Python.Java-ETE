import json
import os
import hashlib
import base64

diretorio_raiz = os.path.dirname(__file__)
diretorio = os.path.join(diretorio_raiz, 'dados/usuarios.json')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_salt():
    return os.urandom(16)  # Gera um salt de 16 bytes (128 bits)

def hash_senha(senha, salt):
    # Utiliza PBKDF2-HMAC-SHA256 para gerar o hash da senha com o salt
    return hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100000)

def salvar_usuarios(usuarios):
    with open(diretorio, 'w') as f:
        json.dump(usuarios, f, indent=2)

def carregar_usuarios():
    try:
        with open(diretorio, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def registrar_transacao(usuario, tipo, valor, destino=None):
    transacao = {
        'tipo': tipo,
        'valor': valor
    }
    if destino:
        transacao['destino'] = destino
    usuario['transacoes'].append(transacao)

def login(usuarios):
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if nome_usuario in usuarios:
        usuario = usuarios[nome_usuario]
        
        # Verifica se a senha foi processada (hashed) ou ainda é a original (sem hash)
        if 'salt' in usuario:
            salt = base64.b64decode(usuario['salt'])  # Decodifica o salt de base64
            senha_hash = hash_senha(senha, salt)

            # Compara o hash gerado com o armazenado
            if senha_hash == base64.b64decode(usuario['senha']):
                return usuario
        else:
            # Se não for um usuário com senha já hasheada, compara diretamente
            if senha == usuario['senha']:
                return usuario
            
    print("Usuário ou senha incorretos.")
    return None

def deposito(usuario):
    valor = float(input("Valor a depositar: R$"))
    if valor > 0:
        usuario['saldo'] += valor
        registrar_transacao(usuario, "Depósito", valor)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido.")

def saque(usuario):
    valor = float(input("Valor a sacar: R$"))
    if valor > 0 and valor <= usuario['saldo']:
        usuario['saldo'] -= valor
        registrar_transacao(usuario, "Saque", valor)
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido ou saldo insuficiente.")

def exibir_transacoes(usuario):
    print("\nHistórico de Transações:")
    if usuario['transacoes']:
        for t in usuario['transacoes']:
            if 'destino' in t:
                print(f"{t['tipo']} de R${t['valor']:.2f} para {t['destino']}")
            else:
                print(f"{t['tipo']} de R${t['valor']:.2f}")
    else:
        print("Nenhuma transação realizada.")

def criar_usuario(usuarios):
    nome_usuario = input("Escolha um nome de usuário: ")
    if nome_usuario in usuarios:
        print("Nome de usuário já existe!")
        passe = input("Pressione Enter para continuar...")
        limpar_terminal()
        return

    senha = input("Escolha uma senha: ")
    salt = gerar_salt()  # Gera um salt único para o usuário
    senha_hash = hash_senha(senha, salt)
    
    saldo_inicial = float(input("Informe o saldo inicial: R$"))  # Solicita o saldo inicial

    usuarios[nome_usuario] = {
        'nome_usuario': nome_usuario,
        'senha': base64.b64encode(senha_hash).decode('utf-8'),  # Armazena o hash da senha em base64
        'salt': base64.b64encode(salt).decode('utf-8'),  # Armazena o salt em base64
        'saldo': saldo_inicial,  # Armazena o saldo inicial
        'transacoes': []
    }

    salvar_usuarios(usuarios)
    print(f"Usuário {nome_usuario} criado com sucesso!")
    passe = input("Pressione Enter para continuar...")
    limpar_terminal()

def transferir(usuario_origem, usuarios):
    nome_destino = input("Nome de usuário do destinatário: ")
    
    if nome_destino not in usuarios:
        print("Usuário de destino não encontrado!")
        return
    
    valor = float(input("Valor a transferir: R$"))
    
    if valor <= 0:
        print("Valor inválido.")
        return
    
    if valor > usuario_origem['saldo']:
        print("Saldo insuficiente para realizar a transferência.")
        return
    
    # Efetuar a transferência
    usuario_origem['saldo'] -= valor
    usuarios[nome_destino]['saldo'] += valor

    # Registrar transação na conta de origem
    registrar_transacao(usuario_origem, "Transferência", valor, nome_destino)
    
    # Registrar transação na conta de destino
    registrar_transacao(usuarios[nome_destino], "Recebimento", valor, usuario_origem['nome_usuario'])
    
    print(f"Transferência de R${valor:.2f} realizada com sucesso para {nome_destino}!")

    salvar_usuarios(usuarios)

def main():
    usuarios = carregar_usuarios()

    while True:
        print("Bem-vindo ao Sistema Bancário!")
        print("1. Já sou usuário")
        print("2. Criar novo usuário")
        print("0. Sair")
        opcao_inicial = input("Escolha uma opção: ")
        limpar_terminal()

        if opcao_inicial == "1":
            usuario_logado = None
            while usuario_logado is None:
                usuario_logado = login(usuarios)
            passe = input("Pressione Enter para continuar...")
            limpar_terminal()

            print(f"\nBem-vindo, {usuario_logado['nome_usuario']}!")

            while True:
                print(f"\nSaldo atual: R${usuario_logado['saldo']:.2f}")
                print("\n1. Realizar Depósito")
                print("2. Realizar Saque")
                print("3. Exibir histórico de transações")
                print("4. Transferir dinheiro")
                print("5. Sair")
                opcao = input("Escolha uma opção: ")
                limpar_terminal()

                if opcao == "1":
                    deposito(usuario_logado)
                elif opcao == "2":
                    saque(usuario_logado)
                elif opcao == "3":
                    exibir_transacoes(usuario_logado)
                elif opcao == "4":
                    transferir(usuario_logado, usuarios)
                elif opcao == "5":
                    break
                else:
                    print("Opção inválida.")
                
                salvar_usuarios(usuarios)
                print(f"\nSaldo atual: R${usuario_logado['saldo']:.2f}")
                passe = input("Pressione Enter para continuar...")
                limpar_terminal()

        elif opcao_inicial == "2":
            criar_usuario(usuarios)

        elif opcao_inicial == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()