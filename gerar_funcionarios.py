import random
import json
from datetime import datetime, timedelta

nomes = [
    "Ana", "Carlos", "Beatriz", "Lenine", "Yago", "Marina", "Lucas", "Paula", "Rafael", "Juliana",
    "Bruno", "Camila", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João", "Larissa", "Mateus"
]
dominios = ["emailficticio.com", "exemplo.com", "teste.com", "empresa.com"]

funcionarios = []
ids = list(range(1, 21))
random.shuffle(ids)

for i, nome in enumerate(nomes):
    # Gera uma data aleatória em 2025
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    data_ferias = (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    # Gera e-mail aleatório
    email = f"{nome.lower()}{random.randint(1,99)}@{random.choice(dominios)}"
    funcionarios.append({
        "id": ids[i],
        "nome": nome,
        "data_ferias": data_ferias,
        "email": email
    })

with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, ensure_ascii=False, indent=2)

print("Arquivo funcionarios.json gerado com sucesso!")
