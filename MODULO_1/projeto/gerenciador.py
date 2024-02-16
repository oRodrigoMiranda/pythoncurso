def adicionar_tarefa(tarefas, nome_tarefa):
    #tarefa: nome da tarefa
    #completada: indica se já foi completada ou nao
    tarefa = {"tarefa": nome_tarefa, "completada":False}
    tarefas.append(tarefa)
    print (f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    print(tarefas)
    return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("\nPrograma finalizado")

