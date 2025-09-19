import json
import sys
from pathlib import Path

def carregar_funcionarios(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler arquivo {caminho}: {e}")
        sys.exit(1)

def salvar_funcionarios(caminho, funcionarios):
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(funcionarios, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo {caminho}: {e}")
        sys.exit(1)
