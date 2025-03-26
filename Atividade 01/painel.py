import os
import subprocess

diretorio_atividades = ".lista"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_arquivos():
    try:
        arquivos = os.listdir(diretorio_atividades)
        arquivos_python = [arquivo for arquivo in arquivos if arquivo.endswith(".py")]
        return arquivos_python
    except FileNotFoundError:
        print(f"Erro: O diretório '{diretorio_atividades}' não foi encontrado.")
        return []

def exibir_painel(arquivos):
    print("Painel de Atividades")
    print("------------------")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")
    print("0. Sair")

def executar_arquivo(arquivo):
    caminho_arquivo = os.path.join(diretorio_atividades, arquivo)
    try:
        subprocess.run(["python", caminho_arquivo], check=True)
        print(f"\n{arquivo} foi finalizado.")
        input("Pressione qualquer tecla para voltar ao painel...")
        limpar_tela()
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o arquivo {arquivo}.")

def main():
    while True:
        limpar_tela()
        arquivos = listar_arquivos()
        if not arquivos:
            print("Nenhum arquivo encontrado no diretório oculto.")
            break
        
        exibir_painel(arquivos)
        
        try:
            escolha = int(input("Escolha uma atividade para executar (ou 0 para sair): "))
            if escolha == 0:
                print("Encerrando o programa.")
                break
            elif 1 <= escolha <= len(arquivos):
                executar_arquivo(arquivos[escolha - 1])
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
