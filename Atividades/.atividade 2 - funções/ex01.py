import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
dados_dir = os.path.join(script_dir, "dados")
os.makedirs(dados_dir, exist_ok=True)
arquivo = os.path.join(dados_dir, "tarefas.json")

def carregar_tarefas():
    return json.load(open(arquivo, "r", encoding="utf-8")) if os.path.exists(arquivo) else []

def salvar_tarefas(tarefas):
    json.dump(tarefas, open(arquivo, "w", encoding="utf-8"), indent=4, ensure_ascii=False)

def adicionar_tarefa(descricao, prazo):
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")

def listar_tarefas():
    tarefas = sorted(carregar_tarefas(), key=lambda x: x["prazo"])
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t['descricao']} - {t['prazo']} ({'✔' if t['concluida'] else 'X'})")

def concluir_tarefa(indice):
    tarefas = carregar_tarefas()
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída!")
    else:
        print("Índice inválido.")

def menu():
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Concluir Tarefa\n4. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_tarefa(input("Descrição: "), input("Prazo: "))
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            concluir_tarefa(int(input("Número da tarefa: ")))
        elif opcao == "4":
            break


menu()