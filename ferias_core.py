from datetime import datetime

def dias_para_ferias(data_ferias_str):
    try:
        hoje = datetime.now().date()
        data_ferias = datetime.strptime(data_ferias_str, "%Y-%m-%d").date()
        delta = (data_ferias - hoje).days
        return delta
    except Exception:
        return None

def listar_funcionarios(funcionarios):
    print("\n📅 Dias para as férias de cada funcionário:")
    print("-" * 60)
    for f in funcionarios:
        id_ = f.get("id", "?")
        nome = f.get("nome", "(sem nome)")
        data_ferias = f.get("data_ferias")
        if not data_ferias:
            print(f"[{id_}] {nome}: ❌ Data de férias não informada.")
            continue
        dias = dias_para_ferias(data_ferias)
        if dias is None:
            print(f"[{id_}] {nome}: ❌ Data inválida ({data_ferias})")
        elif dias < 0:
            print(f"[{id_}] {nome}: 🚩 Férias já passaram! ({-dias} dias atrás)")
        elif dias == 0:
            print(f"[{id_}] {nome}: 🎉 Férias começam hoje!")
        else:
            print(f"[{id_}] {nome}: {dias} dia(s) para as férias ({data_ferias})")

def excluir_funcionario_por_id(funcionarios, id_):
    id_int = int(id_)
    novos = [f for f in funcionarios if f.get("id") != id_int]
    removidos = [f for f in funcionarios if f.get("id") == id_int]
    return novos, removidos
