import tkinter as tk
from tkinter import messagebox, simpledialog
from data import carregar_funcionarios, salvar_funcionarios
from ferias_core import dias_para_ferias, listar_funcionarios, excluir_funcionario_por_id
from email_utils import enviar_email_aviso
from pathlib import Path

ARQUIVO_PADRAO = "funcionarios.json"

class FeriasApp:
    def __init__(self, root):
        self.root = root
        root.title("Gestão de Férias")
        root.geometry("500x400")

        self.text = tk.Text(root, height=15, width=60)
        self.text.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()
    # Botão 'Listar Funcionários' removido
        tk.Button(btn_frame, text="Adicionar Funcionário", command=self.adicionar).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Excluir Funcionário", command=self.excluir).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Enviar E-mails", command=self.enviar_emails).pack(side=tk.LEFT, padx=5)
    def adicionar(self):
        nome = simpledialog.askstring("Adicionar Funcionário", "Nome do funcionário:")
        if not nome:
            return
        email = simpledialog.askstring("Adicionar Funcionário", "E-mail do funcionário:")
        if not email:
            return
        data_ferias = simpledialog.askstring("Adicionar Funcionário", "Data das férias (AAAA-MM-DD):")
        if not data_ferias:
            return
        # Validação simples da data
        from datetime import datetime
        try:
            datetime.strptime(data_ferias, "%Y-%m-%d")
        except Exception:
            messagebox.showerror("Erro", "Data inválida. Use o formato AAAA-MM-DD.")
            return
        funcionarios = carregar_funcionarios(ARQUIVO_PADRAO)
        # Gera novo id único
        ids = [f.get("id", 0) for f in funcionarios]
        novo_id = max(ids) + 1 if ids else 1
        novo_func = {"id": novo_id, "nome": nome, "email": email, "data_ferias": data_ferias}
        funcionarios.append(novo_func)
        salvar_funcionarios(ARQUIVO_PADRAO, funcionarios)
        messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado!")
        self.listar()

        self.listar()

    def listar(self):
        self.text.delete(1.0, tk.END)
        if not Path(ARQUIVO_PADRAO).exists():
            self.text.insert(tk.END, f"Arquivo '{ARQUIVO_PADRAO}' não encontrado.\n")
            return
        funcionarios = carregar_funcionarios(ARQUIVO_PADRAO)
        if not funcionarios:
            self.text.insert(tk.END, "Nenhum funcionário cadastrado.\n")
            return
        # Cabeçalho alinhado
        self.text.insert(tk.END, f"{'ID':<4} {'Nome':<15} {'Dias para Férias':>6} {'Data de Férias':>15}\n")
        self.text.insert(tk.END, f"{'-'*4} {'-'*15} {'-'*6} {'-'*15}\n")
        for f in funcionarios:
            id_ = f.get("id", "?")
            nome = f.get("nome", "(sem nome)")
            data_ferias = f.get("data_ferias")
            dias = dias_para_ferias(data_ferias) if data_ferias else "?"
            self.text.insert(tk.END, f"{str(id_):<4} {nome:<15} {str(dias):>6} {str(data_ferias):>15}\n")

    def excluir(self):
        id_ = simpledialog.askstring("Excluir Funcionário", "Digite o ID do funcionário a excluir:")
        if not id_:
            return
        funcionarios = carregar_funcionarios(ARQUIVO_PADRAO)
        novos, removidos = excluir_funcionario_por_id(funcionarios, id_)
        if not removidos:
            messagebox.showerror("Erro", f"Nenhum funcionário com id={id_} encontrado.")
            return
        salvar_funcionarios(ARQUIVO_PADRAO, novos)
        messagebox.showinfo("Sucesso", f"Funcionário removido: [{removidos[0]['id']}] {removidos[0]['nome']}")
        self.listar()

    def enviar_emails(self):
        funcionarios = carregar_funcionarios(ARQUIVO_PADRAO)
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
            messagebox.showinfo("E-mails enviados", f"Total de e-mails enviados: {enviados}")
        else:
            messagebox.showinfo("Aviso", "Nenhum funcionário está a 5 dias das férias.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FeriasApp(root)
    root.mainloop()
