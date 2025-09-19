
#!/usr/bin/env python3
"""
ferias.py - Calcula dias restantes para as férias de cada funcionário

Uso:
  py ferias.py                # Usa funcionarios.json padrão
  py ferias.py caminho/arquivo.json
  py ferias.py del <id> [arquivo.json]
  py ferias.py sendmails [arquivo.json]
"""
import sys
from pathlib import Path
from data import carregar_funcionarios, salvar_funcionarios
from ferias_core import dias_para_ferias, listar_funcionarios, excluir_funcionario_por_id
from email_utils import enviar_email_aviso

ARQUIVO_PADRAO = "funcionarios.json"

def cli():
    args = sys.argv[1:]
    if args and args[0] == "sendmails":
        caminho = args[1] if len(args) > 1 else ARQUIVO_PADRAO
        if not Path(caminho).exists():
            print(f"❌ Arquivo '{caminho}' não encontrado.")
            sys.exit(1)
        funcionarios = carregar_funcionarios(caminho)
        if not funcionarios:
            print("Nenhum funcionário cadastrado para envio de e-mail.")
            return
        enviados = 0
        for f in funcionarios:
            dias = dias_para_ferias(f.get("data_ferias"))
            if dias is not None and 0 <= dias <= 5:
                email = f.get("email")
                nome = f.get("nome")
                data_ferias = f.get("data_ferias")
                if email and enviar_email_aviso(email, nome, data_ferias):
                    enviados += 1
        if enviados:
            print(f"Total de e-mails enviados: {enviados}")
        else:
            print("Nenhum funcionário está a 5 dias das férias.")
    elif args and args[0] == "del":
        if len(args) < 2:
            print("❌ Uso: py ferias.py del <id> [arquivo.json]")
            sys.exit(1)
        id_ = args[1]
        caminho = args[2] if len(args) > 2 else ARQUIVO_PADRAO
        if not Path(caminho).exists():
            print(f"❌ Arquivo '{caminho}' não encontrado.")
            sys.exit(1)
        funcionarios = carregar_funcionarios(caminho)
        if not funcionarios:
            print("Nenhum funcionário cadastrado para exclusão.")
            return
        novos, removidos = excluir_funcionario_por_id(funcionarios, id_)
        if not removidos:
            print(f"❌ Nenhum funcionário com id={id_} encontrado.")
            sys.exit(1)
        salvar_funcionarios(caminho, novos)
        print(f"✅ Funcionário removido: [{removidos[0]['id']}] {removidos[0]['nome']}")
    else:
        caminho = args[0] if args else ARQUIVO_PADRAO
        if not Path(caminho).exists():
            print(f"❌ Arquivo '{caminho}' não encontrado.")
            sys.exit(1)
        funcionarios = carregar_funcionarios(caminho)
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        listar_funcionarios(funcionarios)

if __name__ == "__main__":
    cli()

