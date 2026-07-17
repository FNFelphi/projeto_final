from dados.armazenamento import carregar_tarefas, salvar_tarefas
from interface import tela
from funcionalidades import tarefas as func

def main():
    lista_tarefas = carregar_tarefas()  # carrega ao iniciar o programa

    while True:
        tela.exibir_menu(lista_tarefas)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            func.adicionar_tarefa(lista_tarefas)
        elif opcao == "2":
            func.editar_tarefa(lista_tarefas)
        elif opcao == "3":
            func.excluir_tarefa(lista_tarefas)
        elif opcao == "4":
            func.concluir_tarefa(lista_tarefas)
        elif opcao == "5":
            lista_tarefas[:] = carregar_tarefas()  # atualiza a lista a partir do arquivo
            print("\n✔ Lista atualizada a partir do tarefas.json.")
        elif opcao == "6":
            salvar_tarefas(lista_tarefas)
            print("\nSaindo... Até logo!")
            break
        else:
            print("\n⚠ Opção inválida.")

        tela.pausar()

if __name__ == "__main__":
    main()