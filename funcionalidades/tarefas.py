"""Adicionar, editar, excluir e marcar tarefas como concluídas."""

from dados.armazenamento import salvar_tarefas

PRIORIDADES = {"1": "Alta", "2": "Média", "3": "Baixa"}

def _escolher_prioridade(atual=None):
    """Pede a prioridade ao usuário. Se 'atual' for informado, ENTER a mantém."""
    print("\nPrioridade:  1-Alta   2-Média   3-Baixa")
    extra = f" (ENTER mantém: {atual})" if atual else ""
    opcao = input(f"Escolha{extra}: ").strip()
    if opcao == "" and atual:
        return atual
    return PRIORIDADES.get(opcao, "Média")

def _pedir_indice(tarefas, acao):
    """Pede o número (1-based) de uma tarefa e devolve o índice (0-based)."""
    if not tarefas:
        print("\n⚠ Não há tarefas cadastradas.")
        return None
    try:
        num = int(input(f"\nNúmero da tarefa para {acao} (0 cancela): "))
    except ValueError:
        print("\n⚠ Entrada inválida.")
        return None
    if num == 0:
        return None
    if 1 <= num <= len(tarefas):
        return num - 1
    print("\n⚠ Número inválido.")
    return None

def adicionar_tarefa(tarefas):
    tarefa = input("Tarefa: ").strip()
    if not tarefa:
        print("\n⚠ A tarefa não pode ficar em branco.")
        return

    prioridade = _escolher_prioridade()
    prazo = input("Prazo (dd/mm/aaaa): ").strip()

    tarefas.append({
        "tarefa": tarefa,
        "prioridade": prioridade,
        "prazo": prazo,
        "concluida": False,
    })
    salvar_tarefas(tarefas)
    print("\n✔ Tarefa adicionada!")

def editar_tarefa(tarefas):
    indice = _pedir_indice(tarefas, "editar")
    if indice is None:
        return

    t = tarefas[indice]
    print("(ENTER mantém o valor atual)")

    novo_nome = input(f"Tarefa [{t['tarefa']}]: ").strip()
    if novo_nome:
        t["tarefa"] = novo_nome

    t["prioridade"] = _escolher_prioridade(atual=t["prioridade"])

    novo_prazo = input(f"Prazo [{t['prazo']}]: ").strip()
    if novo_prazo:
        t["prazo"] = novo_prazo

    salvar_tarefas(tarefas)
    print("\n✔ Tarefa atualizada!")

def excluir_tarefa(tarefas):
    indice = _pedir_indice(tarefas, "excluir")
    if indice is None:
        return

    nome = tarefas[indice]["tarefa"]
    if input(f"Confirma excluir '{nome}'? (s/n): ").strip().lower() == "s":
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("\n✔ Tarefa excluída!")
    else:
        print("\nOperação cancelada.")

def concluir_tarefa(tarefas):
    indice = _pedir_indice(tarefas, "concluir/reabrir")
    if indice is None:
        return

    tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
    salvar_tarefas(tarefas)
    status = "concluída" if tarefas[indice]["concluida"] else "reaberta"
    print(f"\n✔ Tarefa {status}!")