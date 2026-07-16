"""Criar, salvar, carregar e atualizar o arquivo tarefas.json."""
import os
import json

# tarefas.json fica na raiz do projeto 
PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_JSON = os.path.join(PASTA_RAIZ, "tarefas.json")

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON. Cria o arquivo vazio se não existir."""
    if not os.path.exists(CAMINHO_JSON):
        salvar_tarefas([])
        return []

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            return json.loads(conteudo) if conteudo else []
    except (json.JSONDecodeError, OSError):
        print("⚠ Não foi possível ler tarefas.json. Iniciando com lista vazia.")
        return []

def salvar_tarefas(tarefas):
    """Salva (ou atualiza) a lista de tarefas no arquivo JSON."""
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)