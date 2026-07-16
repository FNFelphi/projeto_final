"""Cria a "janela" (tela), define título/tamanho e exibe a lista de tarefas."""

import os

LARGURA_JANELA = 55  # define o "tamanho" da janela no terminal
TITULO_JANELA = "GERENCIADOR DE TAREFAS"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def exibir_titulo():
    """Desenha o cabeçalho da janela com o título definido."""
    print("=" * LARGURA_JANELA)
    print(TITULO_JANELA.center(LARGURA_JANELA))
    print("=" * LARGURA_JANELA)


def exibir_lista(tarefas):
    """Mostra a lista onde as tarefas aparecem, em formato de tabela."""
    print("\n--- Lista de Tarefas ---\n")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print(f"{'Nº':<4}{'Tarefa':<22}{'Prioridade':<12}{'Prazo':<12}{'Status':<10}")
    print("-" * LARGURA_JANELA)
    for i, t in enumerate(tarefas, start=1):
        status = "Concluída" if t["concluida"] else "Pendente"
        print(f"{i:<4}{t['tarefa']:<22}{t['prioridade']:<12}{t['prazo']:<12}{status:<10}")

def exibir_menu(tarefas):
    """Monta a tela completa: janela + lista + opções do menu."""
    limpar_tela()
    exibir_titulo()
    exibir_lista(tarefas)
    print("\n1. Adicionar tarefa")
    print("2. Editar tarefa")
    print("3. Excluir tarefa")
    print("4. Marcar/Desmarcar concluída")
    print("5. Atualizar lista")
    print("6. Sair")
    print("-" * LARGURA_JANELA)