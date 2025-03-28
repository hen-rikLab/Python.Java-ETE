import os
import subprocess

diretorio_raiz = os.path.dirname(__file__)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_pastas(caminho):
    try:
        itens = os.listdir(caminho)
        pastas = [item for item in itens if os.path.isdir(os.path.join(caminho, item))]
        return pastas
    except FileNotFoundError:
        print(f"Erro: O diretório '{caminho}' não foi encontrado.")
        return []

def listar_arquivos(caminho):
    try:
        itens = os.listdir(caminho)
        arquivos_python = [item for item in itens if item.endswith(".py")]
        return arquivos_python
    except FileNotFoundError:
        print(f"Erro: O diretório '{caminho}' não foi encontrado.")
        return []

def exibir_painel_pastas(pastas):
    print("Painel de Atividades")
    print("------------------")
    for i, pasta in enumerate(pastas, start=1):
        print(f"{i}. {pasta}")
    print("0. Sair")

def exibir_painel_arquivos(arquivos):
    print("Arquivos Python")
    print("------------------")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")
    print("0. Voltar")

def executar_arquivo(arquivo, caminho):
    caminho_arquivo = os.path.join(caminho, arquivo)
    try:
        subprocess.run(["python", caminho_arquivo], check=True)
        print(f"\n{arquivo} foi finalizado.")
        input("Pressione Enter para voltar ao painel...")
        limpar_tela()
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o arquivo {arquivo}.")

def navegar_pastas():
    caminho_atual = diretorio_raiz
    while True:
        limpar_tela()
        pastas = listar_pastas(caminho_atual)
        exibir_painel_pastas(pastas)
        
        try:
            escolha = int(input("Escolha uma pasta para acessar (ou 0 para sair): "))
            if escolha == 0:
                return
            elif 1 <= escolha <= len(pastas):
                caminho_pasta = os.path.join(caminho_atual, pastas[escolha - 1])
                navegar_arquivos(caminho_pasta)
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def navegar_arquivos(caminho_pasta):
    while True:
        limpar_tela()
        arquivos = listar_arquivos(caminho_pasta)
        exibir_painel_arquivos(arquivos)
        
        try:
            escolha = int(input("Escolha um arquivo para executar (ou 0 para voltar): "))
            if escolha == 0:
                return
            elif 1 <= escolha <= len(arquivos):
                executar_arquivo(arquivos[escolha - 1], caminho_pasta)
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    navegar_pastas()
    print("Encerrando o programa.")

if __name__ == "__main__":
    main()