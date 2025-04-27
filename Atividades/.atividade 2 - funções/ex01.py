import json
import os

diretorio_raiz = os.path.dirname(__file__)
diretorio = os.path.join(diretorio_raiz, 'dados/tarefas.json')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_tarefas():
    if not os.path.exists('dados'):
        os.makedirs('dados')
    try:
        with open(diretorio, 'r') as f:
            tarefas = json.load(f)
            for t in tarefas:
                if "feito" not in t:
                    t["feito"] = False
            return tarefas
    except:
        return []

def salvar_tarefas(tarefas):
    with open(diretorio, 'w') as f:
        json.dump(tarefas, f, indent=2)

def adicionar_tarefa(tarefas):
    desc = input("Descrição: ")
    prazo = input("Prazo: ")
    tarefas.append({"descricao": desc, "prazo": prazo, "feito": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['prazo'])
    for i, t in enumerate(tarefas_ordenadas):
        status = "✔️" if t['feito'] else "❌"
        print(f"{i+1}. {t['descricao']} - {t['prazo']} {status}")
    passe = input("Pressione Enter para continuar...")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    n = int(input("Número da tarefa para concluir: ")) - 1
    if 0 <= n < len(tarefas):
        tarefas[n]['feito'] = True
    else:
        print("Número inválido.")

def main ():
    tarefas = carregar_tarefas()
    while True:
        print("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n0. Sair")
        op = input("Opção: ")
        limpar_terminal()

        if op == "1":
            adicionar_tarefa(tarefas)
        elif op == "2":
            listar_tarefas(tarefas)
        elif op == "3":
            concluir_tarefa(tarefas)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

        limpar_terminal()

    salvar_tarefas(tarefas)

main()